#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define BUF_SIZE 128 /*the fixed stack buffer*/
#define MAX_COPY 512 /*larger than BUF_SIZE on purpose (sneaky bug)*/

void win(void); 

/*ret2win target: writes markers/ret2win.txt and attempts to read protected decoy.txt*/

static void vulnerable_copy(const unsigned char *input, size_t n) {
    char buf[BUF_SIZE];
    /*copy n bytes from input into buf WITHOUT checking n against BUF_SIZE */
    /* That's the bug! */
    memcpy(buf, input, n);
}

static void parse_log(const char *path) {
    /* read the whole file into a heap buffer, fclose() it THEN call vulnerable_copy(input, n) so the overflow reaches only this frame's saved return address*/
    if (path == NULL) {perror("parse_log: null path"); return; }
    FILE *log_file = fopen(path, "rb");
    if (log_file == NULL) {perror("parse_log: fopen"); return;}
    unsigned char *input = malloc(MAX_COPY + 1);
    if (input == NULL) {
        perror("parse_log: malloc");
        fclose(log_file);
        return;
    }
    size_t n = fread(input, 1, MAX_COPY + 1, log_file);
    int read_failed = ferror(log_file);
    int close_failed = fclose(log_file);
    if (read_failed) {
        perror("parse_log: didn't read");
        free(input);
        return;
    }
    if (close_failed) {
        perror("parse_log: didn't close");
        free(input);
        return;
    }
    if (n > MAX_COPY) {
        perror("parse_log: read too many bytes");
        free(input);
        return;
    }
    size_t copy_len = n < BUF_SIZE ? n : BUF_SIZE;
    vulnerable_copy(input, copy_len);
    free(input);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {return EXIT_FAILURE;}

    parse_log(argv[1]);
    return EXIT_SUCCESS;
}
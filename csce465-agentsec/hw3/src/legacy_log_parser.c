#include <string.h>

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
}
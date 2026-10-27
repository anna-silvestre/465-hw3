#include <string.h>

#define BUF_SIZE 128 /*the fixed stack buffer*/
#define MAX_COPY 512 /*larger than BUF_SIZE on purpose (sneaky bug)*/

void win(void); 

/*ret2win target: writes markers/ret2win.txt and attempts to read protected decoy.txt*/

static void secure_copy(const unsigned char *input, size_t n) {
    char buf[BUF_SIZE];
    
}

static void parse_log(const char *path) {
    /* read the whole file into a heap buffer, fclose() it THEN call secure_copy(input, n) so the overflow reaches only this frame's saved return address*/
    
}
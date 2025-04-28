// This is a simple C program that defines a Point structure and provides functions to manipulate it.
#include <stdio.h>

typedef struct {
    float x;
    float y;
} Point;

void init_point(Point *p, float x, float y) {
    p->x = x;
    p->y = y;
}

void translate(Point *p, float dx, float dy) {
    p->x += dx;
    p->y += dy;
}

void print_point(Point *p) {
    printf("Point at (%f, %f)\n", p->x, p->y);
}

int main() {
    Point p;
    init_point(&p, 1.0, 2.0);
    print_point(&p);
    translate(&p, 3.0, 4.0);
    print_point(&p);
    return 0;
}
EOF
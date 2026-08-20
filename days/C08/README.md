# C08 - C Piscine @ 42

Eighth module of the C Piscine. This project is a series of small, independent
exercises: mostly headers, macros, and two small functions that work together.

## Rules

- No forbidden functions unless explicitly allowed per exercise.
- Compiled by Moulinette with `-Wall -Wextra -Werror` using `gcc`.
- Must pass `norminette` — launched with the `-R CheckDefine` flag for header
  exercises (`ex01`, `ex02`).
- No extra files in your turn-in directories beyond what's asked.
- A harder exercise won't count if an easier one isn't fully working.

## Exercises

| # | Directory | File(s) to turn in | Allowed functions |
|---|-----------|---------------------|--------------------|
| 00 | `ex00/` | `ft.h` | None |
| 01 | `ex01/` | `ft_boolean.h` | None |
| 02 | `ex02/` | `ft_abs.h` | None |
| 03 | `ex03/` | `ft_point.h` | None |
| 04 | `ex04/` | `ft_strs_to_tab.c` | `malloc`, `free` |
| 05 | `ex05/` | `ft_show_tab.c` | `write` |

---

### ex00 — `ft.h`

A header containing only the prototypes of:

```c
void ft_putchar(char c);
void ft_swap(int *a, int *b);
void ft_putstr(char *str);
int  ft_strlen(char *str);
int  ft_strcmp(char *s1, char *s2);
```

No implementation required, just the prototypes (and the usual include guard).

---

### ex01 — `ft_boolean.h`

Must define a `t_bool` type and the macros/constants needed for this main to
compile and run:

```c
#include "ft_boolean.h"

void ft_putstr(char *str)
{
	while (*str)
		write(1, str++, 1);
}

t_bool ft_is_even(int nbr)
{
	return ((EVEN(nbr)) ? TRUE : FALSE);
}

int main(int argc, char **argv)
{
	(void)argv;
	if (ft_is_even(argc - 1) == TRUE)
		ft_putstr(EVEN_MSG);
	else
		ft_putstr(ODD_MSG);
	return (SUCCESS);
}
```

So `ft_boolean.h` needs to define, at minimum:
- `t_bool` (a type with at least `TRUE`/`FALSE` values)
- `TRUE`, `FALSE`
- `EVEN(nbr)` macro
- `EVEN_MSG` → `"I have an even number of arguments.\n"`
- `ODD_MSG` → `"I have an odd number of arguments.\n"`
- `SUCCESS`

Output depending on `argc`:
```
I have an even number of arguments.
```
or
```
I have an odd number of arguments.
```

---

### ex02 — `ft_abs.h`

A single macro:

```c
#define ABS(Value) ...
```

Replaces `Value` with its absolute value. Must be norm-compliant as a macro
(watch out for classic macro pitfalls — parenthesize everything, since the
argument can be an expression, not just a variable).

---

### ex03 — `ft_point.h`

Defines a `t_point` structure with (at least) `x` and `y` members, so this
compiles:

```c
#include "ft_point.h"

void set_point(t_point *point)
{
	point->x = 42;
	point->y = 21;
}

int main(void)
{
	t_point point;

	set_point(&point);
	return (0);
}
```

---

### ex04 — `ft_strs_to_tab`

```c
struct s_stock_str *ft_strs_to_tab(int ac, char **av);
```

Given `ft_stock_str.h`:

```c
typedef struct s_stock_str
{
	int  size;
	char *str;
	char *copy;
}	t_stock_str;
```

- Converts each string in `av` into one `t_stock_str` element, keeping order.
- `size` = length of the string, `str` = the string itself, `copy` = a
  duplicate of the string.
- Returned array must be allocated, with the last element's `str` set to `0`
  (NULL) as an end-of-array marker.
- Returns `NULL` on error (e.g. allocation failure).
- Only `malloc` and `free` are allowed — no `strlen`/`strdup`/etc.

---

### ex05 — `ft_show_tab`

```c
void ft_show_tab(struct s_stock_str *par);
```

- Iterates the array produced by `ft_strs_to_tab` until the sentinel (`str == NULL`).
- For each element, prints in order, each followed by `'\n'`:
  1. the string (`str`)
  2. the size (`size`)
  3. the copy (`copy`)
- Only `write` is allowed.

`ex04` and `ex05` are meant to be tested together (`ft_strs_to_tab` feeding
`ft_show_tab`), so make sure the array format they agree on (the NULL-`str`
terminator) is respected exactly.

---

## Suggested layout

```
.
├── ex00/ft.h
├── ex01/ft_boolean.h
├── ex02/ft_abs.h
├── ex03/ft_point.h
├── ex04/ft_strs_to_tab.c
└── ex05/ft_show_tab.c
```

## Testing

```bash
# norminette (headers especially need -R CheckDefine)
norminette -R CheckDefine ex01/ft_boolean.h ex02/ft_abs.h

# compile check for ex01 main, ex03 main, etc — write a throwaway main.c
gcc -Wall -Wextra -Werror main.c -o test && ./test
```

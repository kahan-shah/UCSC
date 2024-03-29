// Kahan Shah CSE 13S Part B hashtable.c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashtable.h"
#include "set.h"

typedef struct hashtable {
    int num_slots;
    set_t **slots;
} hashtable_t;

// Create a new (empty) hashtable; return NULL if error.
hashtable_t *hashtable_new(const int num_slots) {
    if (num_slots <= 0) {
        return NULL;
    }

    hashtable_t *ht = malloc(sizeof(hashtable_t));
    if (ht == NULL) {
        return NULL;
    }

    ht->num_slots = num_slots;

    ht->slots = malloc(num_slots * sizeof(set_t *));
    if (ht->slots == NULL) {
        free(ht);
        return NULL;
    }

    for (int i = 0; i < num_slots; i++) {
        ht->slots[i] = set_new();
        if (ht->slots[i] == NULL) {
            for (int j = 0; j < i; j++) {
                set_delete(ht->slots[j], NULL);
            }
            free(ht->slots);
            free(ht);
            return NULL;
        }
    }

    return ht;
}

// Hash function
static unsigned long hash(const char *key) {
    unsigned long hash = 5381;
    int c;

    while ((c = *key++) != '\0') {
        hash = ((hash << 5) + hash) + c;
    }

    return hash;
}

// Insert item, identified by key (string), into the given hashtable.
bool hashtable_insert(hashtable_t *ht, const char *key, void *item) {
    if (ht == NULL || key == NULL || item == NULL) {
        return false;
    }

    int slot = hash(key) % ht->num_slots;

    return set_insert(ht->slots[slot], key, item);
}

// Return the item associated with the given key.
void *hashtable_find(hashtable_t *ht, const char *key) {
    if (ht == NULL || key == NULL) {
        return NULL;
    }

    int slot = hash(key) % ht->num_slots;

    return set_find(ht->slots[slot], key);
}

// Print the whole table.
void hashtable_print(hashtable_t *ht, FILE *fp,
                     void (*itemprint)(FILE *fp, const char *key, void *item)) {
    if (ht == NULL || fp == NULL) {
        return;
    }

    for (int i = 0; i < ht->num_slots; i++) {
        set_print(ht->slots[i], fp, itemprint);
    }
}

// Iterate over all items in the table.
void hashtable_iterate(hashtable_t *ht, void *arg,
                       void (*itemfunc)(void *arg, const char *key, void *item)) {
    if (ht == NULL || itemfunc == NULL) {
        return;
    }

    for (int i = 0; i < ht->num_slots; i++) {
        set_iterate(ht->slots[i], arg, itemfunc);
    }
}

// Delete the whole hashtable.
void hashtable_delete(hashtable_t *ht, void (*itemdelete)(void *item)) {
    if (ht == NULL) {
        return;
    }

    for (int i = 0; i < ht->num_slots; i++) {
        set_delete(ht->slots[i], itemdelete);
    }

    free(ht->slots);
    free(ht);
}


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "set.h"

// Structure for a single node in the set
typedef struct node {
    char *key;
    void *item;
    struct node *next;
} node_t;

// Structure for the set
struct set {
    node_t *head;
};

// Create a new set return NULL if error.
set_t* set_new(void) {
    set_t *set = malloc(sizeof(set_t));
    if (set == NULL)
        return NULL;

    set->head = NULL;
    return set;
}

// Insert item, identified by a key (string), into the given set.
bool set_insert(set_t *set, const char *key, void *item) {
    if (set == NULL || key == NULL || item == NULL)
        return false;

    // Check if the key already exists in the set
    node_t *curr = set->head;
    while (curr != NULL) {
        if (strcmp(curr->key, key) == 0)
            return false; // Key already exists
        curr = curr->next;
    }

    // Create a new node for the item
    node_t *new_node = malloc(sizeof(node_t));
    if (new_node == NULL)
        return false;

    // Copy the key string
    new_node->key = strdup(key);
    if (new_node->key == NULL) {
        free(new_node);
        return false;
    }

    new_node->item = item;
    new_node->next = set->head;
    set->head = new_node;

    return true;
}

// Return the item associated with the given key;
// return NULL if set is NULL, key is NULL, or key is not found.
void* set_find(set_t *set, const char *key) {
    if (set == NULL || key == NULL)
        return NULL;

    node_t *curr = set->head;
    while (curr != NULL) {
        if (strcmp(curr->key, key) == 0)
            return curr->item;
        curr = curr->next;
    }

    return NULL; // Key not found
}

// Print the whole set
void set_print(set_t *set, FILE *fp, void (*itemprint)(FILE *fp, const char *key, void *item)) {
    if (fp == NULL)
        return;

    if (set == NULL) {
        fprintf(fp, "(null)\n");
        return;
    }

    node_t *curr = set->head;
    while (curr != NULL) {
        itemprint(fp, curr->key, curr->item);
        curr = curr->next;
    }
}

// Iterate over all items in the set, in undefined order.
// Call eahc given function on each item
void set_iterate(set_t *set, void *arg, void (*itemfunc)(void *arg, const char *key, void *item)) {
    if (set == NULL || itemfunc == NULL)
        return;

    node_t *curr = set->head;
    while (curr != NULL) {
        itemfunc(arg, curr->key, curr->item);
        curr = curr->next;
    }
}

// Helper function to free a node and its key
static void free_node(node_t *node, void (*itemdelete)(void *item)) {
    if (node == NULL)
        return;

    if (itemdelete != NULL)
        itemdelete(node->item);

    free(node->key);
    free(node);
}

// Delete the whole set; ignore NULL set
// Provide a function that will delete each item 
void set_delete(set_t *set, void (*itemdelete)(void *item)) {
    if (set == NULL)
        return;

    node_t *curr = set->head;
    while (curr != NULL) {
        node_t *next = curr->next;
        free_node(curr, itemdelete);
        curr = next;
    }

    free(set);
}


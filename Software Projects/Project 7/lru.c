#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lru.h"

typedef struct lru_entry_t lru_entry_t;

struct lru_entry_t {
    char *key;              // Key for the cache entry
    void *value;            // Value associated with the key
    lru_entry_t *prev;      // Pointer to the previous entry in the linked list
    lru_entry_t *next;      // Pointer to the next entry in the linked list
};

struct lru_t {
    int capacity;           // Maximum capacity of the cache
    int size;               // Current size of the cache
    lru_entry_t *head;      // Pointer to the head (most recently used entry) of the linked list
    lru_entry_t *tail;      // Pointer to the tail (least recently used entry) of the linked list
    lru_entry_t **hash_table;   // Hash table to store cache entries
    void (*evict_cb)(void *);   // Callback function to be called when an entry is evicted
};

static unsigned long hash(const char *str) {
    unsigned long hash = 5381;
    int c;
    while ((c = *str++)) {
        hash = ((hash << 5) + hash) + c;
    }
    return hash;
}

// Create a new LRU cache with the given capacity
lru_t *lru_new(const int capacity) {
    if (capacity <= 0)
        return NULL;

    lru_t *lru = (lru_t *)malloc(sizeof(lru_t));
    if (lru == NULL)
        return NULL;

    lru->capacity = capacity;
    lru->size = 0;
    lru->head = NULL;
    lru->tail = NULL;
    lru->hash_table = (lru_entry_t **)calloc(capacity, sizeof(lru_entry_t *));
    if (lru->hash_table == NULL) {
        free(lru);
        return NULL;
    }

    lru->evict_cb = NULL;

    return lru;
}

// Insert a new key-value pair into the LRU cache
bool lru_insert(lru_t *lru, const char *key, void *value) {
    if (lru == NULL || key == NULL || value == NULL)
        return false;

    unsigned long index = hash(key) % lru->capacity;

    lru_entry_t *new_entry = (lru_entry_t *)malloc(sizeof(lru_entry_t));
    if (new_entry == NULL)
        return false;

    new_entry->key = strdup(key);
    new_entry->value = value;
    new_entry->prev = NULL;
    new_entry->next = NULL;

    if (lru->size == 0) {
        lru->head = new_entry;           // The new entry becomes the head and tail
        lru->tail = new_entry;
    } else {
        new_entry->next = lru->head;      // Make the new entry the new head
        lru->head->prev = new_entry;
        lru->head = new_entry;
    }

    if (lru->hash_table[index] != NULL) {
        lru_entry_t *temp = lru->hash_table[index];
        while (temp != NULL) {
            if (strcmp(temp->key, key) == 0) {
                free(new_entry->key);
                free(new_entry);
                return false;  // Key already exists in the cache
            }
            temp = temp->next;
        }
    }

    new_entry->next = lru->hash_table[index];
    if (lru->hash_table[index] != NULL)
        lru->hash_table[index]->prev = new_entry;
    lru->hash_table[index] = new_entry;

    lru->size++;

    // Evict the least recently used entry if the cache exceeds the capacity
    if (lru->size > lru->capacity) {
        lru_entry_t *last_entry = lru->tail;
        lru->tail = last_entry->prev;
        if (lru->tail != NULL)
            lru->tail->next = NULL;
        else
            lru->head = NULL;

        unsigned long last_entry_index = hash(last_entry->key) % lru->capacity;
        if (lru->hash_table[last_entry_index] == last_entry) {
            lru->hash_table[last_entry_index] = NULL;
        } else {
            lru_entry_t *temp = lru->hash_table[last_entry_index];
            while (temp != NULL) {
                if (temp->next == last_entry) {
                    temp->next = NULL;
                    break;
                }
                temp = temp->next;
            }
        }

        if (lru->evict_cb != NULL)
            lru->evict_cb(last_entry->value);

        free(last_entry->key);
        free(last_entry);

        lru->size--;
    }

    return true;
}

// Find the value associated with the given key in the LRU cache
void *lru_find(lru_t *lru, const char *key) {
    if (lru == NULL || key == NULL)
        return NULL;

    unsigned long index = hash(key) % lru->capacity;

    lru_entry_t *temp = lru->hash_table[index];
    while (temp != NULL) {
        if (strcmp(temp->key, key) == 0) {
            // Move the found entry to the front of the cache (MRU position)
            if (temp != lru->head) {
                if (temp == lru->tail)
                    lru->tail = temp->prev;

                if (temp->prev != NULL)
                    temp->prev->next = temp->next;
                if (temp->next != NULL)
                    temp->next->prev = temp->prev;

                temp->next = lru->head;
                temp->prev = NULL;
                lru->head->prev = temp;
                lru->head = temp;
            }

            return temp->value;
        }
        temp = temp->next;
    }

    return NULL;  // Key not found in the cache
}

// Delete the LRU cache and free the associated memory
void lru_delete(lru_t *lru, void (*cb)(void *)) {
    if (lru == NULL)
        return;

    lru_entry_t *temp = lru->head;
    while (temp != NULL) {
        lru_entry_t *next = temp->next;
        if (cb != NULL)
            cb(temp->value);
        free(temp->key);
        free(temp);
        temp = next;
    }

    free(lru->hash_table);
    free(lru);
}

// Print the contents of the LRU cache
void lru_print(lru_t *lru, FILE *fp, void (*itemprint)(FILE *fp, const char *key, void *item)) {
    if (fp == NULL || lru == NULL)
        return;

    lru_entry_t *temp = lru->head;
    while (temp != NULL) {
        itemprint(fp, temp->key, temp->value);
        temp = temp->next;
    }
}

// Iterate over the entries in the LRU cache and call the given function on each entry
void lru_iterate(lru_t *lru, void *arg, void (*itemfunc)(void *arg, const char *key, void *item)) {
    if (lru == NULL || itemfunc == NULL)
        return;

    lru_entry_t *temp = lru->head;
    while (temp != NULL) {
        itemfunc(arg, temp->key, temp->value);
        temp = temp->next;
    }
}


import math
from io import StringIO


class minHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.nodes = [0] * self.capacity

    def get_left_idx(self, parentIdx): return 2*parentIdx + 1

    def get_right_idx(self, parentIdx): return 2*parentIdx + 2

    def get_parent_idx(self, childIdx): return (childIdx-1)//2

    def has_left_child(self, idx): return self.get_left_idx(idx) < self.size

    def has_right_child(self, idx): return self.get_right_idx(idx) < self.size

    def has_parent(self, idx): return self.get_parent_idx(idx) >= 0

    def left_child(self, idx): return self.nodes[self.get_left_idx(idx)]

    def right_child(self, idx): return self.nodes[self.get_right_idx(idx)]

    def parent(self, idx): return self.nodes[self.get_parent_idx(idx)]

    def swap(self, idx1, idx2):
        temp = self.nodes[idx1]
        self.nodes[idx1] = self.nodes[idx2]
        self.nodes[idx2] = temp

    def ensure_extra_capacity(self):
        # If new level is needed, we need to double the size of the array
        # because # of leaf nodes on last layer equals size of rest of the heap + 1
        if self.size == self.capacity:
            self.nodes.extend([0] * 2*self.capacity)
            self.capacity *= 2

    def peek(self):
        if self.size == 0:
            return None
        return self.nodes[0]

    def add(self, item):
        self.ensure_extra_capacity()
        self.nodes[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        idx = self.size - 1
        while self.has_parent(idx) and self.parent(idx) > self.nodes[idx]:
            self.swap(self.get_parent_idx(idx), idx)
            idx = self.get_parent_idx(idx)

    def heapify_down(self):
        idx = 0
        while self.has_left_child(idx):
            smaller_idx = self.get_left_idx(idx)
            if self.has_right_child(idx) and self.right_child(idx) < self.left_child(idx):
                smaller_idx = self.get_right_idx(idx)

            if self.nodes[idx] < self.nodes[smaller_idx]:
                break
            self.swap(idx, smaller_idx)
            idx = smaller_idx

    def poll(self):
        # Removes the minimum element
        if self.size == 0:
            return None
        item = self.nodes[0]
        self.nodes[0] = self.nodes[self.size-1]
        self.nodes[self.size-1] = 0
        self.size -= 1
        self.heapify_down()
        return item


#source https://bit.ly/38HXSoU
def show_tree(tree, total_width=60, fill=' '):
    """Pretty-print a tree.
    total_width depends on your input size"""
    output = StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i+1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns = 2**row
        col_width = int(math.floor((total_width * 1.0) / columns))
        if n != 0:
            output.write(str(n).center(col_width, fill))
            last_row = row
    print (output.getvalue())
    print ('-' * total_width)
    return


if __name__ == '__main__':
    heap = minHeap(10)
    heap.add(10)
    heap.add(17)
    heap.add(25)
    #show_tree(heap.nodes)
    heap.add(20)
    heap.add(15)
    heap.add(27)
    heap.add(1)
    heap.add(12)

    show_tree(heap.nodes)
    print(heap.peek())
    heap.poll()
    show_tree(heap.nodes)
    heap.poll()
    show_tree(heap.nodes)
    heap.poll()
    show_tree(heap.nodes)
    heap.poll()
    show_tree(heap.nodes)














class MinHeap:

    def __init__(self):
        self.heap_list = [None]
        self.count = 0

        # difine heap helper methods,
    # which take an index as a parameter and return correspoinding parent or child index
    def parent_idx(self, idx):
        return idx // 2

    def left_child_idx(self, idx):
        return idx * 2

    def right_child_idx(self, idx):
        return idx * 2 + 1

    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    def heapify_down(self):
        idx = 1
        while self.child_present(idx):
            print("Heapifying down")
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent
                idx = smaller_child_idx

    def add(self, element):
        "Adding {} to {}.".format(element, self.heap_list)
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    def retrieve_min(self):

        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[1]
        print("Removing: {0} from {1}".format(min, self.heap_list))
        self.heap_list[1] = self.heap_list[self.count]
        self.heap_list.pop()
        self.count -= 1
        print("Last element moved to first: {0}".format(self.heap_list))
        self.heapify_down()
        return min

    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            print("There is only a left child")
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                print("Left child is smaller.")
                return self.left_child_idx(idx)
            else:
                print("Right child is smaller.")
                return self.right_child_idx(idx)

    def heapify_up(self):
        idx = self.count
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                tmp = self.heap_list[self.parent_idx(idx)]
                print("swapping {0} with {1}".format(tmp, self.heap_list[idx]))
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)
        print("HEAP RESTORED! {0}".format(self.heap_list))
        print("")

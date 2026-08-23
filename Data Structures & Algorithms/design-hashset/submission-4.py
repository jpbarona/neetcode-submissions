N_BUCKETS = 997

class MyHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(N_BUCKETS)] 
       
        def hash_function(x: int) -> int:
            return x % N_BUCKETS
        
        self.h = hash_function
        

    def add(self, key: int) -> None:
        bucket = self.buckets[self.h(key)]
        exists = key in bucket
        if exists:
            return
        
        bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[self.h(key)]
        exists = key in bucket
        if not exists:
            return
        
        bucket.remove(key)
        
    def contains(self, key: int) -> bool:
        bucket = self.buckets[self.h(key)]
        return key in bucket
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
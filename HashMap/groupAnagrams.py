from collections import defaultdict
class GroupAnagrams:
    
    def groupanagram(self,strs):
       anagram_dict=defaultdict(list)
       result=[]
       for s in strs:
           sorted_s=tuple(sorted(s))
           anagram_dict[sorted_s].append(s)
       for val in anagram_dict.values():
           result.append(val)
       return result

if __name__=="__main__":
    strs=["eat","tea","tan","ate","nat","bat","cat"]
    obj=GroupAnagrams()
    anagrams=obj.groupanagram(strs)
    print(anagrams)

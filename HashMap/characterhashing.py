class CharacterHashing:
    def characterHashing(self,st,arr):
        s_arr=list(st)
        hash_arr=[0]*26
        for s in s_arr:
            ind=ord(s)-97
            hash_arr[ind]+=1
        output={}
        for k in arr:
            ind=ord(k)-97
            output[k]=hash_arr[ind]
        return output

obj=CharacterHashing()
s="azyxyyzaaaabx"
arr=['d','a','y','x']
hashed_output=obj.characterHashing(s,arr)
print(hashed_output)

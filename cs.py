import numpy as np
def cs(a,b):
	dot_product=np.dot(a,b)
	norm_a= np.linalg.norm(a)
	norm_b= np.linalg.norm(b)
	return dot_product/(norm_a*norm_b+1)

def Ocs(movie_id):
	mat=cm.toarray()
	res=[]
	for i in range(len(mat)):
		curr=[]
		for j in range(len(mat)):
			if(i==j):
				curr.append(1)
			else:
				curr.append(round(cs(mat[i],mat[j])))
		res.append(curr)
	
	res =np.reshape(res,[len(mat),len(mat)])
	return res[movie_id]




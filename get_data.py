#对不同的split生成openmatch的文件
import json
def get_q_d():
	for t in ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', \
	'17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']:
		query_file=open('/home/dihe/Projects/data/QG/queries'+t,'r').readlines()
		doc_file=open('/home/dihe/Projects/data/QG/corpus'+t,'r').readlines()
		w=open('/home/dihe/Projects/data/QG/q_d'+str(t)+'.jsonl','w', encoding="utf-8")
		
		for line1,line2 in zip(query_file,doc_file):
			temp_data={}
			line1=json.loads(line1)
			line2=json.loads(line2)
			assert line1["pos_doc_id"]==line2['_id']
			temp_data['query']=line1['text']
			temp_data['doc']=line2["text"]
			temp_data['query_id']=line1["_id"]
			temp_data['doc_id']=line1["pos_doc_id"]
			temp_data['retrieval_score']=0

			w.write("{}\n".format(json.dumps(temp_data)))
	w.close()

def get_filter_queries():
	#qd_score={}
	#rewrite queries file
	pass
if __name__ == '__main__':
	get_q_d()
	
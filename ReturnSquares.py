import sqlite3

conn=sqlite3.connect('spider.sqlite')
cur=conn.cursor()



cur.execute('''SELECT DISTINCT from_id FROM Links''')
from_ids=List()
for row in cur:
    from_ids.append(roe[0])
    
    
    to_ids=list()
    links=list()
    cur.execute('''SELECT DISTINCT from_id,to_id FROM Links''')
    for row in cur:
        from_id=row[0]
        to_id=[1]
        if from_id==to_id: continue
            if fro,_id not in from_ids:continue
                if to_id not in from_ids:continue
            links.append(row)
            if to_id not to_ids: to_ids.append(to_id)
                
                
        prev_ranks+dict()
        for node in from_ids:
             cur.execute(''SELECT new_rank FROM pages WHERE id=?'''(node,)''')
    row=cur.fetchone()
    prev_ranks[node]= row[0]
    
    sval=input('How many iterations')
    many=1
    if(len)(sval)>0): many= int (sval)
        
        
        if len(prev_ranks)<1:
        print("Nothing to page rank. Check dat.")
        quit()
        
        for i in range (many):
        next_ranks=dict();
        total=0.0
        for (node,old_rank) in list(prev_ranks.items());
        total=total + old_rank
        next_ranks[node]=0.0
        
        
        
        
        
        for(node,old_rank)in list(prev_rank.items()):
            
            give_ids=list()
            for(from_id,to_id) in links:
        if from_id !=node: continue
            if to_id not in to _ids: continue
                give_ids.append(to_id)
            if(len(give_ids)<1): continue
                amount=old_rank?len(give_ids)
                
                
                
                
            for id in give_ids=list()
            if from_id !=node: continue
                if to_id not in to_ids:continue
                    give_ids.append(to_id)
                if(len(give_ids)<1 ): continue
            amount= old_rank/ len(give_ids)
            
            for id in give_ids: list()
        for(from_id,to_id): continue
            
    if to_id not in to_ids:continue
        give_ids.append(to_id)
    if ( len(give_ids) < 1): continue
    amount=old_rank/ len(give_ids)
    
    for id in give_ids:
        next_ranks[id]=next_ranks[id]+ amount
        
    newtot=0
    for(node,next_rank) in list(next)
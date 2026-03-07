import time 
class TODO:
    todos = [
        # {
        #     'id':'',
        #     'desc':'',
        #     'isCompleted':False
        # }
    ]
    def add_todo(self, id, desc):
        # 1. Take desc from the user
        # 2. We have to create one dict in which we will add todo desc
        # 3. Append the dict inside todo 
        if(len(desc)==0):
            print('Task cannot be empty.')
        else:
            self.todos.append({'id':id,'desc':desc,'isCompleted':False})

    
    def remove_todo(self, id):
            for i in self.todos:
                if(i['id'] == id): self.todos.remove(i)
                else: print(f'id: {id} is not present')
            print(f'id: {id} removed successfully')
    
    def display_todos(self):
        print(self.todos)
    
    def update_todo(self, id, new_desc):
        for i in self.todos:
            if(i['id'] == id): 
                i['desc'] = new_desc
            else: 
                print(f'id: {id} is wrong')
        return self.todos
    
    def toggle_mark_as_completed(self, id):
        for i in self.todos:
            if(i['id'] == id and i['isCompleted'] == False): i['isCompleted'] = True
            else: print('Already done')
    
    def completed_todos(self):
        for i in self.todos:
            if(i['isCompleted'] == True): return (i)
            else: print('No todos has been completed')
        return (i)
    
    def incompleted_todos(self):
        for i in self.todos:
            if(i['isCompleted'] == False): return (i)
            else: print('All todos has been completed')
        return (i)
        
# t=TODO() 
# t.add_todo(12345, 'Eat lunch')
# t.display_todos()
# t.update_todo(12345, 'Eat Dinner')
# t.display_todos()
# t.remove_todo(12345)
# t.display_todos()
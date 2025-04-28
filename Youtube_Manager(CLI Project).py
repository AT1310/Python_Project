
import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except:
         return []
def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)
        
def list_all_videos(videos):
    if len(videos)!=0:
        for index,video in enumerate(videos,start=1):
            print('\n')
            print('*'*60)
            print('\n')
            print(f"{index}.Name:{video['Name']},Duration: {video['Time']},Description: {video['Description']}")
    else:
        print('*'*60)
        print('\n')
        print('No Data Available Currently')
    print('\n')
    print('*'*60)
    print('\n')
        
def add_video(videos):
    name=input('Enter video name:')
    time=input('Enter video time:')
    description=input('Enter the details about the video:')
    videos.append({'Name':name,'Time':time,'Description':description})
    save_data_helper(videos)
    print('\n')
    print('*'*60)
    print('\n')
    print('Video named',name,'has been added')
    print('\n')
    print('*'*60)
def update_video(videos):
    list_all_videos(videos)
    index=int(input('Enter the video number you want to update: '))
    if 1<= index <=len(videos):
        name=input('Enter the name of video: ')
        time=input('Enter the time of video: ')
        description=input('Enter the details about the video: ')
        videos[index-1]={'Name':name,'Time':time,'Description':description}
        save_data_helper(videos)
        print('\n')
        print('*'*60)
        print('\n')
        print('Video number',index,'is updated')
        print('\n')
        print('*'*60)
        print('\n')
    else:
        print('\n')
        print('*'*60)
        print('\n')
        print('Invalid index selected')
        print('\n')
        print('*'*60)
        print('\n')
        
def delete_video(videos):
    list_all_videos(videos)
    index=int(input('Enter the video number to be deleted: '))

    if 1<= index<= len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print('\n')
        print('*'*60)
        print('\n')
        print('Video number',index,'is deleted')
        print('\n')
        print('*'*60)
        print('\n')
        
    else:
        print('\n')
        print('*'*60)
        print('\n')
        print("Invalid video index selected")
        print('\n')
        print('*'*60)
        print('\n')
        

    
def main():
    videos=load_data()
    while True:
        print('Youtube_Manager | Make a choice')
        print('1. List all Youtube Videos')
        print('2. Add a Youtube video')
        print('3. Update a video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice=input('Enter your choice: ')
        print('\n')
        
        
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print('\n')
                print('*'*60)
                print('\n')
                print('Thankyou for using the app')
                print('\n')
                print('*'*60)
                print('\n')
                break
            case _:
                print('\n')
                print('*'*60)
                print('\n')
                print('Invalid choice')
                print('\n')
                print('*'*60)
                print('\n')
        
main()



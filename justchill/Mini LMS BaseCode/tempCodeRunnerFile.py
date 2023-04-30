def Update_Student(student_json_file,Mobile_Number,detail_to_be_updated,new_detail):
    f=open(student_json_file,'r+')
    content=json.load(f)
    for i in range(len(content)):
        if content[i]["Mobile Number"]==Mobile_Number:
            try:
                a=content[i][detail_to_be_updated]
            except KeyError:
                return False
            content[i][detail_to_be_updated]=new_detail
            f.seek(0)
            f.truncate()
            json.dump(content,f)
            f.close()
            return True
    f.close()
    return False
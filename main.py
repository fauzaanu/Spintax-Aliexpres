from csv import reader

with open('muslim_fashion.csv', newline='') as csvfile:
    csvrader = reader(csvfile, delimiter=',', quotechar='"')
    specefic_rows_format = list(csvrader) #to read specefic rows later on
    datarows = len(specefic_rows_format) #amount of rows
    
    print(datarows)


    #Making it easier to modify when ali decides to change stuff
    #if csv file naming is different need to change these to match
    name_index = specefic_rows_format[0].index("Product Name")
    image_link_index = specefic_rows_format[0].index("Product Image Url")
    #video_link_index = specefic_rows_format[0].index("Video Url")
    aff_link_index = specefic_rows_format[0].index("Click url")

    #print(f"{specefic_rows_format[0]} {datarows}")
    main = ""
    start = 0
   
    for i in range(datarows):
        print(i)
        header = [] #define a list 
        header = specefic_rows_format[i]

        image_link = header[image_link_index]
        
        image_link = image_link.replace("jpg_220x220.jpg","jpg_350x350.jpg") #changing image resolution

        #video_link = header[video_link_index]
        name  =  header[name_index]
        aff_link = header[aff_link_index]

        if "https" in name: #if the name is a url
            #print("URL WAS DETECTED AT NAME") #ONLY FOR DEBUGGING
            continue

        if "https" not in image_link: #if the name is a url
            #print("URL WAS NOT DETECTED AT IMAGE LINK") #ONLY FOR DEBUGGING
            continue

        # if video_link.find("https") == -1: #if the name is a url
        #     #print("URL WAS NOT DETECTED AT VIDEO LINK") #ONLY FOR DEBUGGING
        #     continue
            
        if "https" not in aff_link: #if the name is a url
            #print("URL WAS NOT DETECTED AT AFF LINK") #ONLY FOR DEBUGGING
            continue
        
        main = main + "<p>" + f"<a href='{aff_link}'>{name}</a></p><img src='{image_link}' /> |"

    
    final_text = "{"+main+"}"
    final_text= final_text.replace("|}","}")
    #print(final_text)

    f = open("muslim_fashion.html", "w")
    f.write(final_text)
    f.close()

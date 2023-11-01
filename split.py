import os
import pypdfium2 as pdfium

path_name = '/home/user/Data3/CircularData'

#write a function to get the images from the pdf and split images into individual folders (First Page, Middle Pages, Last pages) and save them in logical folders according to the pdf name
def get_images_and_split_into_folders(pdf_file):
    #print(pdf_file)
    pdf = pdfium.PdfDocument(pdf_file)

    try:
        pno = len(pdf)
        if pno == 1:
            page = pdf.get_page(0)
            pil_image = page.render(
                scale=1,
                rotation=0,
                crop=(0, 0, 0, 0)).to_pil()
            # os.makedirs("C:\\Users\\ramak\\Pictures\\pdf2img\\{}".format(pdf_file.split('\\')[-1].split('.')[0]), exist_ok=True)
            # pil_image.save("C:\\Users\\ramak\\Pictures\\pdf2img\\{}\\image_{}.png".format(pdf_file.split('\\')[-1].split('.')[0],1))
            os.makedirs('/home/user/Data3/Split_Images/first_page', exist_ok=True)
            pil_image.save('/home/user/Data3/Split_Images/first_page/img_fp_{}_{}.png'.format(pdf_file.split('/')[-2],pdf_file.split('/')[-1].split('.')[0]))
        elif pno == 2:
            #first_page
            fpage = pdf.get_page(0)
            pil_image = fpage.render(
                scale=1,
                rotation=0,
                crop=(0, 0, 0, 0)).to_pil()
            # os.makedirs("C:\\Users\\ramak\\Pictures\\pdf2img\\{}".format(pdf_file.split('\\')[-1].split('.')[0]), exist_ok=True)
            # pil_image.save("C:\\Users\\ramak\\Pictures\\pdf2img\\{}\\image_{}.png".format(pdf_file.split('\\')[-1].split('.')[0],1))
            os.makedirs('/home/user/Data3/Split_Images/first_page', exist_ok=True)
            pil_image.save('/home/user/Data3/Split_Images/first_page/img_fp_{}_{}.png'.format(pdf_file.split('/')[-2],pdf_file.split('/')[-1].split('.')[0]))

            #last page
            lpage = pdf.get_page(1)
            pil_image = lpage.render(
                scale=1,
                rotation=0,
                crop=(0, 0, 0, 0)).to_pil()
            # os.makedirs("C:\\Users\\ramak\\Pictures\\pdf2img\\{}".format(pdf_file.split('\\')[-1].split('.')[0]), exist_ok=True)
            # pil_image.save("C:\\Users\\ramak\\Pictures\\pdf2img\\{}\\image_{}.png".format(pdf_file.split('\\')[-1].split('.')[0],2)) 
            os.makedirs('/home/user/Data3/Split_Images/last_page', exist_ok=True)
            pil_image.save('/home/user/Data3/Split_Images/last_page/img_lp_{}_{}.png'.format(pdf_file.split('/')[-2],pdf_file.split('/')[-1].split('.')[0]))

        elif pno>2:
            #first page
            fpage = pdf.get_page(0)
            pil_image = fpage.render(
                scale=1,
                rotation=0,
                crop=(0, 0, 0, 0)).to_pil()
            # os.makedirs("C:\\Users\\ramak\\Pictures\\pdf2img\\{}".format(pdf_file.split('\\')[-1].split('.')[0]), exist_ok=True)
            # pil_image.save("C:\\Users\\ramak\\Pictures\\pdf2img\\{}\\image_{}.png".format(pdf_file.split('\\')[-1].split('.')[0],1))
            os.makedirs('/home/user/Data3/Split_Images/first_page', exist_ok=True)
            pil_image.save('/home/user/Data3/Split_Images/first_page/img_fp_{}_{}.png'.format(pdf_file.split('/')[-2],pdf_file.split('/')[-1].split('.')[0]))

            #middle pages
            for page_number in range(1,pno-1):
                page = pdf.get_page(page_number)
                pil_image = page.render(
                    scale=1,
                    rotation=0,
                    crop=(0, 0, 0, 0)).to_pil()
                # os.makedirs("C:\\Users\\ramak\\Pictures\\pdf2img\\{}".format(pdf_file.split('\\')[-1].split('.')[0]), exist_ok=True)
                # pil_image.save("C:\\Users\\ramak\\Pictures\\pdf2img\\{}\\image_{}.png".format(pdf_file.split('\\')[-1].split('.')[0],page_number+1))
                os.makedirs('/home/user/Data3/Split_Images/middle_page', exist_ok=True)
                pil_image.save('/home/user/Data3/Split_Images/middle_page/img_mp_{}_{}_{}.png'.format(page_number+1, pdf_file.split('/')[-1].split('.')[0],pdf_file.split('/')[-2]))

            #last pages
            lpage = pdf.get_page(pno-1)
            pil_image = lpage.render(
                scale=1,
                rotation=0,
                crop=(0, 0, 0, 0)).to_pil()
            # os.makedirs("C:\\Users\\ramak\\Pictures\\pdf2img\\{}".format(pdf_file.split('\\')[-1].split('.')[0]), exist_ok=True)
            # pil_image.save("C:\\Users\\ramak\\Pictures\\pdf2img\\{}\\image_{}.png".format(pdf_file.split('\\')[-1].split('.')[0],pno))
            os.makedirs('/home/user/Data3/Split_Images/last_page', exist_ok=True)
            pil_image.save('/home/user/Data3/Split_Images/last_page/img_lp_{}_{}.png'.format(pdf_file.split('/')[-2],pdf_file.split('/')[-1].split('.')[0]))
    except:
        pass

#get_images_and_split_into_folders('/home/user/Data3/CircularData/CS Harayana/971.pdf')
lisst=[]
for a,b,c in os.walk(path_name):
    for i in os.listdir(a):
        aa = os.path.join(a,i)
        #with open('a.txt','a') as f:
        #    f.write(aa+'\n')
        lisst.append(aa)
        #if i.endswith('.pdf'):
#        get_images_and_split_into_folders(aa)
print(lisst[0])
for i in lisst:
    if i.endswith('.pdf'):
        print(i)
        get_images_and_split_into_folders(i)

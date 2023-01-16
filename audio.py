import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar :
    selected =option_menu('Meme Mit',
        ['Fresh',
        'Absurd'],
        default_index=0)
    

if(selected == 'Fresh'):
    st.title('Fresh Mim')
    from PIL import Image

    genre = st.radio(
    "Lu mau ngeliat meme apa?",
    ('Audio Meme', 'Video Meme', 'Image Meme','Random'))

if genre == 'Audio Meme':
    st.write('Kamu memilih Audio mim.')
    rating = st.slider('Rating',0,10)
    konfirmasi =st.button('Masukkan Rating Keseluruhan')
    if konfirmasi :
         rating = 1,10
         st.success('Berhasil Mengreting😂👌')
    audio_file = open ('bang al bang al @naplive7.mp3','rb')
    audio_bytes =audio_file.read()
    st.title("Bang AL Bang AL 💩")
    st.audio(audio_bytes,format ='bang al bang al @naplive7.mp3')
    st.title("Zetaa 👉👈")
    audio_file = open ('Vestia Zeta aa jangan dong, yada.. Sound Effect.mp3','rb')
    audio_bytes =audio_file.read()
    st.audio(audio_bytes,format ='Vestia Zeta aa jangan dong, yada.. Sound Effect.mp3')
    st.title('😭')
    audio_file= open('BANG AL KAPAN MAIN NYA BANG.mp3','rb')
    audio_bytes=audio_file.read()
    st.audio(audio_bytes,format = 'BANG AL KAPAN MAIN NYA BANG.mp3')

if genre == 'Video Meme':
    st.write("Kamu memilih Video mim.")
    rating = st.slider('Rating',0,10)
    konfirmasi =st.button('Masukkan Rating Keseluruhan')
    if konfirmasi :
      rating = 1,10
      st.success('Berhasil Mengreting😂👌')
    st.title("Legenda sed")
    video =open("Tak_berjudul_79_720p.mov","rb")
    st.video(video)
    st.title('...')
    video1 =open("lv_0_20230111191912.mp4","rb")
    st.video(video1)
    st.title('pria yang baik hati ini memperbaiki meja 😊')
    video3=open('lv_0_20230105233552.mp4','rb')
    st.video(video3)
    st.title('📳')
    video5 =open('e47dfdf1f5d16507aea0539a19999b2f.mp4','rb')
    st.video(video5)
    st.title('Bang messi')
    video8 =open('Artinya Apa Bang Messi Tapi Bang Messinya Beneran Messi....mp4','rb')
    st.video(video8)
    st.title('🤨')
    video9 =open('km_20230104_1080p.mp4','rb')
    st.video(video9)


if genre == 'Image Meme':
    st.write('Kamu memilih Image mim.')
    rating = st.slider('Rating',0,10)
    konfirmasi =st.button('Masukkan Rating Keseluruhan')
    if konfirmasi :
      rating = 1,10
      st.success('Berhasil Mengreting😂👌')
    st.title('Foto Andhar')
    image1= Image.open("Andhar.jpg")
    st.image(image1)
    st.title('???')
    image2=Image.open("meme image pkl.jpg")
    st.image(image2)
    st.title('👍')
    image3 =Image.open('kerja bagus.jpg')
    st.image(image3)
    st.title('Congratz RRQ')
    image4 =Image.open('rrq.jpg')
    st.image(image4)

if genre == 'Random':
    st.write('Kamu memilih Random mim.')  
    rating = st.slider('Rating',0,10)
    konfirmasi =st.button('Masukkan Rating Keseluruhan')
    if konfirmasi :
      rating = 1,10
      st.success('Berhasil Mengreting😂👌')  
    video2 =open('lv_0_20230115203753.mp4','rb')
    st.video(video2)
    st.title('===============================')
    video4=open('791C7801-6BA6-4638-9065-BB13E89CC69D.mov','rb')
    st.video(video4)
    st.title('===============================')
    video6 =open('lv_0_20221230172518','rb')
    st.video(video6)
    st.title('===============================')
    video7 =open('lv_0_20221225085148.mp4','rb')
    st.video(video7)
    st.title('===============================')
    video10 =open('2F4EC5C7-BC8A-4E1C-9A38-0B8253B3FE15.mov','rb')
    st.video(video10)





    

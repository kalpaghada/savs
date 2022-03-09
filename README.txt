Information regarding the dependencies for each component is included in a README in corresponding subfolders.
--------------------------------------------------------------------------------------------------------------

To avoid unintended dependency errors, use Ubuntu Bionic Beaver.

Main dependencies
  python 3.6.9
  pip 9.0.1 &
  Corresponding tensorflow version (1.14 or <2.0)
    pip3 install --upgrade tensorflow==1.14
    
If using VirtualBox, use version 6.0.18

--------------------------------------------------------------------------------------------------------------

Installation
1. Download and install all the dependencies for each component/subfolder.
2. Download and store a collection of videos that you would want to perform searches on in /imagedetection/video_database subfolder.
3. Now, in the /imagedetection subfolder, run detect2.py. The description of each script file and what it does is given in the README.txt of each component subfolder. The directory location inside all these scripts may have to be changed manually as of now.
4. Run condense.py.
5. In the /extractaudio subfolder, run generate_audio.py.
6. Run caption.py.

You've completed preprocessing the data! Now, execute run.py from the main folder to perform a search.
To run the database integrity checker, execute the script /integritychecker/analyze.py

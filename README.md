<H1> Recosteam - COP3530 - Project 2 </h1>
Arjun Sujith, Adrian Estevez, and Seth Cruz's submission for Project 2.

<h2> Running the command-line interface</h2>

While our GUI app is not complete, we defer to a command-line app -- essentially a full demo of the app functionality. 
To run it, ensure you have Python 3 installed and open a terminal. Then, follow these steps(replace "name_of_folder" with your preference):

1. Run ***git clone https://github.com/00adrn/Project-2---Video-Game-Recommender name_of_folder*** to clone the repo, if you have git installed. You could also download directly and unzip.
2. ***cd name_of_folder*** to go to the newly created folder.
3. Now, there are some options. Either:
   * run  ***python -m pip install -r requirements.txt*** to install python dependencies into your main system interpreter.
   * create a venv within folder_name by running **python -m venv .venv***, then run ***source .venv/bin/activate***(macOS/linux/unix-based) or ***./.venv/Scripts/activate.bat***  (windows) and then do the above step. In this case, the python dependencies downloaded are localized to the app directory.
   * or, simply run ***python setup.py***. This does both of the above for you, and prompts you to run the appropriate activation script.
4. Download this folder(or the files): https://drive.google.com/drive/folders/1IsZEdEkIyactDXV-sGs5R-pO83StQypp?usp=drive_link and unzip its two files into the **{system_path}/name_of_folder/preprocessing/data**. Make sure they are taken out of the original downloaded folder and put into that directory. These files are quite large, so the initial download might take some time.
5. Finally, making sure you are in **name_of_folder** in the terminal, run: ***python CLI.py***  .


<h2> (Defunct) Running the program (note: we are still working on the full app)</h2>

The following are the steps to run the program:

- Ensure that you have NodeJS and Python 3 installed on your computer, along with Node Package Manager and, on the python side, install numpy, pandas, pyarrow, nltk, scikit-learn and joblib.
  
- Open the project in your terminal.

- run the command "python app.py" to intialize backend server
  
- Access the frontend folder : cd frontend
  
- Run and the initialized the server by running the following command in the terminal: npm run dev

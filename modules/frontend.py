import os, shutil, time

def update_frontend(repository, project):
    MODULES = 'node_modules'
    ADMIN = 'juancamr'
    
    start = time.time()
    os.system('sudo su')
    exists = os.path.exists(f'./{repository}')
    if (not exists):
        os.system(f'git clone https://github.com/{ADMIN}/{repository}')
        install_modules(repository, project)
    else:
        try:
            shutil.move(f'./{repository}/{MODULES}', f'./{MODULES}')
        except FileNotFoundError as e: 
            install_modules(repository, project)

        os.system(f'rm -r ./{repository}')
        os.system(f'git clone https://github.com/{ADMIN}/{repository}')
        shutil.move(f'./{MODULES}', f'./{repository}/{MODULES}')
        os.chdir(f'./{repository}')
        os.system('npm install')
        os.system('ng build')
        os.system(f'cp -r ./dist ../../{project}/dist')

        end = time.time()
        print(f'Pagina actualizada en {round(end - start)} segundos.')

def install_modules(repository, project):
    os.chdir(f'./{repository}')
    os.system('npm install')
    os.chdir('../')
    update_frontend(repository, project)
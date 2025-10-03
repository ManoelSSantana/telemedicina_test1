import subprocess
import sys
import os
from threading import Thread
import webbrowser

def check_nodejs():
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Node.js não está instalado. Por favor, instale Node.js de https://nodejs.org/")
        webbrowser.open("https://nodejs.org/")
        return False

def setup_frontend(project_root):
    frontend_path = os.path.join(project_root, "frontend")
    if not os.path.exists(frontend_path):
        print("Configurando frontend...")
        os.makedirs(os.path.join(frontend_path, "src"), exist_ok=True)
        os.chdir(frontend_path)
        subprocess.run(["npm", "init", "-y"], shell=True)
        subprocess.run(["npm", "install", "react", "react-dom", "vite", "@vitejs/plugin-react"], shell=True)
        os.chdir(project_root)
    return True

def run_backend(project_root):
    backend_path = os.path.join(project_root, "backend")
    os.chdir(backend_path)
    subprocess.run([sys.executable, "-m", "uvicorn", "app.main:app", "--reload"])

def run_frontend(project_root):
    if not check_nodejs():
        return
    frontend_path = os.path.join(project_root, "frontend")
    if not setup_frontend(project_root):
        return
    os.chdir(frontend_path)
    subprocess.run(["npm", "run", "dev"], shell=True)

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    backend_thread = Thread(target=run_backend, args=(project_root,))
    frontend_thread = Thread(target=run_frontend, args=(project_root,))

    print("Iniciando o backend...")
    backend_thread.start()
    
    print("Iniciando o frontend...")
    frontend_thread.start()

    try:
        backend_thread.join()
        frontend_thread.join()
    except KeyboardInterrupt:
        print("\nEncerrando os serviços...")
        os.chdir(project_root)
        sys.exit(0)
    except KeyboardInterrupt:
        print("\nEncerrando os serviços...")
        os.chdir(project_root)
        sys.exit(0)
        
    if not setup_frontend():
        os.chdir("frontend")
        subprocess.run(["npm", "run", "dev"], shell=True)

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)
    
    backend_thread = Thread(target=run_backend)
    frontend_thread = Thread(target=run_frontend)

    print("Iniciando o backend...")
    backend_thread.start()
    
    print("Iniciando o frontend...")
    frontend_thread.start()

    try:
        backend_thread.join()
        frontend_thread.join()
    except KeyboardInterrupt:
        print("\nEncerrando os serviços...")
        os.chdir(project_root)  # Changed from original_path to project_root
        sys.exit(0)
        backend_thread.join()
        frontend_thread.join()
    except KeyboardInterrupt:
        print("\nEncerrando os serviços...")
        os.chdir(project_root)
        sys.exit(0)
        sys.exit(0)

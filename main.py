# verificando se tem as bibliotecas para rodar o projeto
try:
    import glfw
except ImportError:
    print("Execute este código 'pip install glfw' ou 'pip3 install glfw'")
    exit()

def main():
    if not glfw.init():
        return
    
    window = glfw.create_window(640,480,"teste", None, None)

    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)

    while not glfw.window_should_close(window):

        glfw.swap_buffers(window)

        glfw.poll_events()
    
    glfw.terminate()

main()
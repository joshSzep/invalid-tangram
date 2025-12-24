import pygame
import moderngl


def main():
    pygame.init()

    # Request a Core OpenGL 3.3 context (what ModernGL expects by default).
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
    pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
    pygame.display.gl_set_attribute(
        pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
    )

    # Optional but nice.
    pygame.display.gl_set_attribute(pygame.GL_DOUBLEBUFFER, 1)
    pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
    pygame.display.gl_set_attribute(pygame.GL_STENCIL_SIZE, 8)

    screen = pygame.display.set_mode(
        (0, 0),
        flags=pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN,
    )
    pygame.display.set_caption("Invalid Tangram")

    # Sanity check: what did we actually get?
    gl_version = (
        pygame.display.gl_get_attribute(pygame.GL_CONTEXT_MAJOR_VERSION),
        pygame.display.gl_get_attribute(pygame.GL_CONTEXT_MINOR_VERSION),
    )
    print("Pygame GL context version:", gl_version)
    print(
        "Pygame GL profile:",
        pygame.display.gl_get_attribute(pygame.GL_CONTEXT_PROFILE_MASK),
    )

    # Create ModernGL context from the *existing* active context
    ctx = moderngl.create_context(require=330)
    print("ModernGL:", ctx.version_code, ctx.info["GL_VERSION"])

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        ctx.clear(0.1, 0.1, 0.1, 1.0)
        pygame.display.flip()
        clock.tick(120)

    pygame.quit()


if __name__ == "__main__":
    main()

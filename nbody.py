import pygame
import random
import math
import sys

WIDTH, HEIGHT = 800, 600
# Gravitational constant
G = 1.0
# Simulation time step
DT = 0.1

class Body:
    def __init__(self, pos, vel, mass):
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.mass = mass

    def draw(self, screen):
        radius = max(2, int(self.mass))
        pygame.draw.circle(screen, (255, 255, 255), self.pos, radius)


def compute_forces(bodies):
    n = len(bodies)
    for i in range(n):
        for j in range(i + 1, n):
            b1 = bodies[i]
            b2 = bodies[j]
            r = b2.pos - b1.pos
            dist_sq = r.length_squared()
            if dist_sq == 0:
                continue
            dist = math.sqrt(dist_sq)
            force_mag = G * b1.mass * b2.mass / dist_sq
            direction = r / dist
            force = force_mag * direction
            b1.vel += force / b1.mass * DT
            b2.vel -= force / b2.mass * DT


def update_bodies(bodies):
    compute_forces(bodies)
    for b in bodies:
        b.pos += b.vel * DT
        # Bounce off window edges to keep bodies visible
        if b.pos.x < 0:
            b.pos.x = 0
            b.vel.x *= -1
        elif b.pos.x > WIDTH:
            b.pos.x = WIDTH
            b.vel.x *= -1
        if b.pos.y < 0:
            b.pos.y = 0
            b.vel.y *= -1
        elif b.pos.y > HEIGHT:
            b.pos.y = HEIGHT
            b.vel.y *= -1


def add_body(bodies, position):
    mass = random.uniform(5, 20)
    # Start with a small random velocity so bodies move gradually
    vel = (random.uniform(-5, 5), random.uniform(-5, 5))
    bodies.append(Body(position, vel, mass))


def remove_nearest(bodies, position, radius=10):
    if not bodies:
        return
    pos_vec = pygame.Vector2(position)
    nearest = min(bodies, key=lambda b: (b.pos - pos_vec).length())
    if (nearest.pos - pos_vec).length() <= radius:
        bodies.remove(nearest)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("N-Body Simulation")
    clock = pygame.time.Clock()

    bodies = []
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    add_body(bodies, event.pos)
                elif event.button == 3:  # right click
                    remove_nearest(bodies, event.pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    bodies.clear()

        update_bodies(bodies)

        screen.fill((0, 0, 0))
        for b in bodies:
            b.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()

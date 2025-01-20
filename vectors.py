from dataclasses import dataclass
from typing import List
import math

@dataclass
class Vector:
    components: List[float]

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector([a * scalar for a in self.components])

    def dot(self, other: 'Vector') -> float:
        return sum(a * b for a, b in zip(self.components, other.components))

    def magnitude(self) -> float:
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self) -> 'Vector':
        mag = self.magnitude()
        return Vector([a / mag for a in self.components])

    def cross(self, other: 'Vector') -> 'Vector':
        if len(self.components) == 3 and len(other.components) == 3:
            a1, a2, a3 = self.components
            b1, b2, b3 = other.components
            return Vector([
                a2 * b3 - a3 * b2,
                a3 * b1 - a1 * b3,
                a1 * b2 - a2 * b1
            ])
        else:
            raise ValueError("Cross product is only defined for 3-dimensional vectors")

    def angle_with(self, other: 'Vector') -> float:
        dot_product = self.dot(other)
        magnitudes = self.magnitude() * other.magnitude()
        return math.acos(dot_product / magnitudes)

    def projection_onto(self, other: 'Vector') -> 'Vector':
        dot_product = self.dot(other)
        other_magnitude_squared = other.magnitude() ** 2
        scalar_projection = dot_product / other_magnitude_squared
        return other * scalar_projection

    def is_orthogonal_to(self, other: 'Vector') -> bool:
        return math.isclose(self.dot(other), 0.0)

    def __repr__(self) -> str:
        return f"Vector({self.components})"

# Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print(f"v1: {v1}")
print(f"v2: {v2}")
print(f"v1 + v2: {v1 + v2}")
print(f"v1 - v2: {v1 - v2}")
print(f"v1 * 3: {v1 * 3}")
print(f"v1 . v2: {v1.dot(v2)}")
print(f"|v1|: {v1.magnitude()}")
print(f"v1 normalized: {v1.normalize()}")
print(f"v1 x v2: {v1.cross(v2)}")
print(f"Angle between v1 and v2: {v1.angle_with(v2)} radians")
print(f"Projection of v1 onto v2: {v1.projection_onto(v2)}")
print(f"Are v1 and v2 orthogonal? {v1.is_orthogonal_to(v2)}")
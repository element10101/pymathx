from .validate_type import validate_type

class Rectangle:
  """
  Represents a rectangle.
  """
  def __init__(self, *, l:float=None, w:float=None, a:float=None):
    """
    Creates a rectangle.

    @doc [
      @param l: float -> The length of the rectangle. @keyword
      @param w: float -> The width of the rectangle. @keyword
      @param a: float -> The area of the rectangle. @keyword
    ]
    """
    self.l = l
    self.w = w
    self.a = a
  def area(self):
    """
    Returns the area of the rectangle.

    @doc [
      @returns float | None
      @raises TypeError | None
    ]
    """
    if self.l != None and self.w != None:
      return self.l * self.w if self.a is None else self.a
    else:
      raise TypeError("Either length or width is None")
  def perimeter(self):
    """
    Returns the perimeter of the rectangle.

    @doc [
      @returns float | None
      @raises TypeError | None
    """
    if self.l != None and self.w != None:
      return (2 * self.l) + (2 * self.w)
    else:
      raise TypeError("Either length or width is None")

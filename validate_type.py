def validate_type(var, t):
  """
  Validates if a variable is the specified type. Raises a @class TypeError if it is not the specified type.

  @doc [
    @param var: any -> The variable to validate.
    @param t: any -> The type to validate to.
    @returns bool | None
    @raises TypeError | None
  ]
  """
  if type(var) != t:.
    raise TypeError(f"{var.__name__} is not of type {t}")
  else:
    return True

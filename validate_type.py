def validate_type(var, t):
  """
  Validates if a variable is the specified type.

  @doc [
    @param var: any -> The variable to validate.
    @param t: any -> The type to validate to.
    @returns bool
  ]
  """
  return type(var) == t

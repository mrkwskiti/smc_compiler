from ..binary import TwosComplement

class Register:
  def __init__(self):
    self._register = [
      TwosComplement(0, 32),
      TwosComplement(0, 32),
      TwosComplement(0, 32),
      TwosComplement(0, 32),
      TwosComplement(0, 32),
      TwosComplement(0, 32),
      TwosComplement(0, 32),
      TwosComplement(0, 32),
    ]
  
  def get_register(self, reg_no):
    return self._register[reg_no]

  def set_register(self, reg_on, value):
    if reg_on is 0:
      """ if set reg_on 0, do noting """
      return
    self._register[reg_on] = TwosComplement(value, 32)

  def __iter__(self):
    self.register_iter = iter(self._register)
    return self.register_iter

  def __next__(self):
    return next(self.register_iter)

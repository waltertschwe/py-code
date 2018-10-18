# The below section of code from the Python Wiki is designed to do something particular,
# can you explain what it does?

import time
import math

def retry(tries, delay=3, backoff=2):
  if backoff <= 1:
    raise ValueError("backoff must be greater than 1")

  tries = math.floor(tries)
  if tries < 0:
    raise ValueError("tries must be 0 or greater")

  if delay <= 0:
    raise ValueError("delay must be greater than 0")

  def deco_retry(f):
    def f_retry(*args, **kwargs):
      mtries, mdelay = tries, delay # make mutable

      rv = f(*args, **kwargs) # first attempt
      while mtries > 0:
        if rv is True: # Done on success
          return True

        mtries -= 1        # consume an attempt
        time.sleep(mdelay) # wait...
        mdelay *= backoff  # make future wait longer

        rv = f(*args, **kwargs) # Try again

      return False # Ran out of tries :-(

    return f_retry
  return deco_retry

@retry(tries=3)
def test_retry(input):
    print("Retry: " + input)

test_retry("testing... retry decorator")

## it is going to keep calling the function until the amount of tries runs out

## in all fairness, unlike the other two questions which were straight forward
## I would have been able to give you a general idea of what was going on with the code above.
## Using the decorator pattern is not something I have used a lot with my Python code.

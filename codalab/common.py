'''
This module exports some simple names used throughout the CodaLab bundle system:
  - Constants that should eventually be moved to some configuration file.
  - The various CodaLab error classes, with documentation for each.
  - The State class, an enumeration of all legal bundle states.
  - precondition, a utility method that check's a function's input preconditions.
'''
import os


BUNDLE_FILE_PORT = 2800
BUNDLE_RPC_PORT = 2801
CODALAB_HOME = os.path.expanduser('~/.codalab')


class IntegrityError(ValueError):
  '''
  Raised by the model when there is a database integrity issue.

  Indicates a serious error that either means that there was a bug in the model
  code that left the database in a bad state, or that there was an out-of-band
  database edit with the same result.
  '''


class PreconditionViolation(ValueError):
  '''
  Raised when a value generated by one module fails to satisfy a precondition
  required by another module.

  This class of error is serious and should indicate a problem in code, but it
  it is not an AssertionError because it is not local to a single module.
  '''


class UsageError(ValueError):
  '''
  Raised when user input causes an exception. This error is the only one for
  which the command-line client suppresses output.
  '''


class State(object):
  '''
  An enumeration of states that a bundle can be in.
  '''
  CREATED = 'created'
  STAGED = 'staged'
  RUNNING = 'running'
  READY = 'ready'
  FAILED = 'failed'

  OPTIONS = set([CREATED, STAGED, RUNNING, READY, FAILED])
  FINAL_STATES = set([READY, FAILED])


def precondition(condition, message):
  if not condition:
    raise PreconditionViolation(message)

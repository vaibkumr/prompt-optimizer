.. prompt-optimizer documentation master file, created by
   sphinx-quickstart on Fri Apr  7 15:53:36 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to PromptOptimizer!
============================================
Minimize LLM token complexity to save API costs and model computations.

PromptOptimizer is a Python library designed to minimize the token complexity of natural language understanding (NLU) systems, thereby reducing API costs and computational overhead. 
It offers a range of optimizers to achieve this optimization while maintaining the integrity of important sections of the prompt.

Disclaimer
----------------
There is a compression vs performance tradeoff -- the increase in compression comes at the cost of loss in model performance. The tradeoff can be greatly mitigated by chosing the right optimize for a given task. There is no single optimizer for all cases. There is no Adam here.


Getting Started
----------------


.. toctree::
   :maxdepth: 2
   :caption: Contents:

Documentations
=========================
Following are the documentations for optimzier and metrics:


Prompt Optimizer
=========================
.. automodule:: prompt_optimizer.poptim
   :members:


Metrics
=========================
.. automodule:: prompt_optimizer.metric
   :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

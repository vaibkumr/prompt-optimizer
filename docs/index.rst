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

| How to get started using PromptOptimizer and minimize token complexity.

- `Quickstart Guide <./getting_started/getting_started.html>`_

| Compression metrics for sanity checks and logging.

- `Optimization Metrics <./getting_started/metrics.html>`_

| PromptOptimizer CLI (Coming soon)

- `CLI <./getting_started/cli.html>`_

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   :name: getting_started
   :hidden:

   getting_started/getting_started.md
   getting_started/metrics.md
   getting_started/cli.md

Extending PromptOptimizer
-------------------------
You can create custom prompt optimizers 

- `Custom PromptOptimizers <./extend/custom_optims.html>`_

It is also easy to create custom metrics

- `Custom Metrics <./extend/custom_metrics.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Extending PromptOptimizer
   :name: extend
   :hidden:

   extend/custom_optims.md
   extend/custom_metrics.md

Evaluations
-----------
There is no one prompt optimizer that works for all tasks. 
Through evaluations over a diverse set of tasks we can make the right choice of optimizer for a new task.

Extending Evaluations to include more tasks 

- `Extending Evaluations <./evaluations/extending_evals.html>`_

Evaluating prompt optiimzers is same as evaluating LLMs before and after optimizations and measuring the differences. We thus provide OpenAI Evals Compatiblity to facilitate this.

- `OpenAI Evals Compatiblity <./evaluations/openai_evals.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Evaluations
   :name: evals
   :hidden:

   evaluations/extending_evals.md
   evaluations/openai_evals.md

Cost-Performance Tradeoff
-------------------------
The reduction in cost often comes with a loss in LLM performance. Almost every optimizer have hyperparameters that control this tradeoff. 

- `Cost-Performance Tradeoff <./theory/cost_performance_tradeoff.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Cost-Performance Tradeoff
   :name: tradeoff
   :hidden:

   theory/cost_performance_tradeoff.md


Reference Documentations
=========================
Full documentation on all classes and methods for PromptOptimizer.

- `Reference Documentations <./reference.html>`_
- `Installation Guide <./getting_started/installation.html>`_

.. toctree::
   :maxdepth: 1
   :caption: Reference Documentations
   :name: reference
   :hidden:

   ./getting_started/installation.md
   ./reference.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

# call knime with variables from python
have you ever wanted to call a knime workflow with globally defined variables? Here's how.

```
python knime_python_example.py
```
This `knime_python_example.py` file won't work out of the box.  You will need to edit and set `-workflowFile='/path/to/file.knwf'` to wherever your workflow of interest is location and you will have to approriately edit your variables in `-workflow.variable` with as many variables as your workflow has defined. if they are defaulted, you don't need this command. remember `-workflow.variable` syntax is `name,value,type`. The `knime_python_example.py` shows `int` and `String` example variables.  

Some additional notes:

1) you can swap the file `-workflowFile` for directory `-workflowDir='path/to/directory`. Don't forget that to make this work any string need to single quoted ('). 
2) all the other arguments after knime and before your paths etc are just settings I click. it doesn’t open the GUI, it doesn’t save, the workflow is rest, and it closes your terminal upon completion of the workflow
3) a lot of stuff will be printed to your terminal. in my experience when you see ---Registering Weka Editors--- that means you did it correctly!
4) Additional knime command line info can be found here: https://forum.knime.com/t/decent-documentation-for-command-line-execution-with-variables/31680

Cheers.

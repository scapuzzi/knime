import os

os.system("knime --launcher.suppressErrors -nosplash -nosave -reset -application org.knime.product.KNIME_BATCH_APPLICATION -workflowFile='/path/to/file.knwf' -workflow.variable=myvariable1,999,int -workflow.variable=myvariable2,foo,String")

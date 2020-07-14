from django.db import models
from supervisor.models import TableEvaluation

# Create your models here.

class TableEvaluationIndicator(models.Model):
    table_evaluation_indicator_col_id = models.IntegerField(db_column='Table_Evaluation_Indicator_col_id',
                                                            primary_key=True)  # Field name made lowercase.
    table_evaluation_indicator_col_name = models.CharField(db_column='Table_Evaluation_Indicator_col_Name',
                                                           max_length=50)  # Field name made lowercase.
    # table_evaluation_indicator_col_root = models.CharField(db_column='Table_Evaluation_Indicator_col_Root',
    #                                                        max_length=50)  # Field name made lowercase.
    # table_evaluation_indicator_col_parent_id = models.IntegerField(db_column='Table_Evaluation_Indicator_col_Parent_id',
    #                                                                blank=True, null=True)  # Field name made lowercase.
    # table_evaluation_indicator_col_parent_name = models.CharField(
    #     db_column='Table_Evaluation_Indicator_col_Parent_Name', max_length=50, blank=True,
    #     null=True)  # Field name made lowercase.
    table_evaluation_indicator_col_parent_name = models.ForeignKey('self', on_delete=models.PROTECT, db_constraint=False,
                               null=True, blank=True, verbose_name='父部门')
    table_evaluation_indicator_col_weight = models.DecimalField(db_column='Table_Evaluation_Indicator_col_Weight',
                                                                max_digits=10,
                                                                decimal_places=2)  # Field name made lowercase.
    table_evaluation_indicator_col_evaluation_name = models.CharField(
        db_column='Table_Evaluation_Indicator_col_Evaluation_Name', max_length=50)  # Field name made lowercase.
    table_evaluation_indicator_col_administrator_id = models.IntegerField(
        db_column='Table_Evaluation_Indicator_col_Administrator_id')  # Field name made lowercase.
    table_evaluation_indicator_col_administrator_name = models.CharField(
        db_column='Table_Evaluation_Indicator_col_Administrator_Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Table_Evaluation_Indicator'

class TableQuestionContent(models.Model):
    table_question_content_col_question_id = models.AutoField(db_column='Table_Question_Content_col_Question_id', primary_key=True)  # Field name made lowercase.
    table_question_content_col_question_type = models.IntegerField(db_column='Table_Question_Content_col_Question_type',null=True)  # Field name made lowercase.
    # table_question_content_col_dataset_id = models.IntegerField(db_column='Table_Question_Content_col_DataSet_id')  # Field name made lowercase.
    table_question_content_col_indicator_id = models.IntegerField(db_column='Table_Question_Content_col_Indicator_id',null=True)  # Field name made lowercase.
    table_question_content_col_question_number = models.IntegerField(db_column='Table_Question_Content_col_Question_number',null=True)  # Field name made lowercase.
    # table_question_content_col_label = models.IntegerField(db_column='Table_Question_Content_col_Label')  # Field name made lowercase.
    table_question_content_col_auto = models.CharField(db_column='Table_Question_Content_col_Auto', max_length=1,null=True)  # Field name made lowercase.
    # table_question_content_col_specialist = models.CharField(db_column='Table_Question_Content_col_Specialist', max_length=50, blank=True, null=True)  # Field name made lowercase.
    table_question_content_col_marks = models.CharField(db_column='Table_Question_Content_col_Marks', max_length=50,null=True)  # Field name made lowercase.
    table_question_content_col_content = models.TextField(db_column='Table_Question_Content_col_Content',null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Table_Question_Content'

class TableTimeliner(models.Model):
    table_timeliner_col_id = models.AutoField(db_column='Table_Timeliner_col_id', primary_key=True)  # Field name made lowercase.
    table_timeliner_col_start = models.DateField(db_column='Table_Timeliner_col_start')  # Field name made lowercase.
    table_timeliner_col_content = models.CharField(db_column='Table_Timeliner_col_content', unique=True, max_length=255)  # Field name made lowercase.
    table_timeliner_col_end = models.DateField(db_column='Table_Timeliner_col_end')  # Field name made lowercase.
    table_timeliner_col_status = models.CharField(db_column='Table_Timeliner_col_status', max_length=128)  # Field name made lowercase.
    table_timeliner_col_name = models.CharField(db_column='Table_Timeliner_col_name', max_length=128)
    table_timeliner_col_evaluation = models.CharField(db_column='Table_Timeliner_col_evaluation', max_length=128)

    class Meta:
        managed = True
        db_table = 'Table_Timeliner'
        ordering = ['table_timeliner_col_start', 'table_timeliner_col_evaluation']

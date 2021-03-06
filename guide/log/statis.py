"""
迹、数量
迹属性
事件、数量
事件属性
变体、数量
开始活动、结束活动
循环
"""
import pm4py
from pm4py.objects.log.importer.xes.importer import apply as xes_importer
from pm4py.statistics.attributes.log.get import *
from pm4py.statistics.traces.generic.log import case_statistics
from pm4py.statistics.start_activities.log.get import get_start_activities
from pm4py.statistics.end_activities.log.get import get_end_activities


def base_info(log):
    trace_count = len(log)
    all_trace_attributes = get_all_trace_attributes_from_log(log)
    print("日志共有%d条迹，有%d种属性" % (trace_count, len(all_trace_attributes)), all_trace_attributes)

    event_count = 0
    for trace in log:
        event_count += len(trace)
    all_event_attributes = get_all_event_attributes_from_log(log)
    print("日志共有%d个事件，有%d种属性" % (event_count, len(all_event_attributes)), all_event_attributes)

    activity_attr_value = get_attribute_values(log, 'concept:name')
    activity_attr_value_count = len(activity_attr_value)
    print("日志共有%d种活动" % activity_attr_value_count, list(activity_attr_value.keys()))

    variants = case_statistics.get_variant_statistics(log)
    variant_count = len(variants)
    print("日志共有%d种不同的迹" % variant_count, variants)

    start_activities = get_start_activities(log)
    print("开始活动", list(start_activities.keys()))
    end_activities = get_end_activities(log)
    print("结束活动", list(end_activities.keys()))


def cycle_info(log):
    # 每个案例中有多少活动发生了重复
    from pm4py.statistics.rework.cases.log.get import apply as get_rework_case
    aa = get_rework_case(log)
    print(aa)
    # 日志中活动重复发生了多少次
    from pm4py.statistics.rework.log.get import apply as get_rework_log
    bb = get_rework_log(log)
    print(bb)



if __name__ == '__main__':
    # log = xes_importer('../statics/log/running-example.xes')
    log = xes_importer('../statics/log/receipt.xes')
    base_info(log)
    cycle_info(log)



# -*- coding: utf-8 -*-

from diaphora_ida import _diff_or_export
import idc
import idaapi

idaapi.autoWait()
file_out = idaapi.get_input_file_path() + '.sqlite'
_diff_or_export(use_ui=False, file_out=file_out)


idc.Exit(0)

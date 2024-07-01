from arif import *

def from_pram_to_obrat(entry, result_label):

    user_text = f"Результат обратного кода: {alg_from_pram_to_obrat(entry.get())}"
    result_label.config(text=user_text)


def from_pram_to_dop(entry, result_label):
    user_text = f"Результат дополнительного кода: {alg_from_pram_to_dop(entry.get())}"
    result_label.config(text=user_text)


def perevesti(entry, result_label, result_dop_label):
    from_pram_to_obrat(entry, result_label)
    from_pram_to_dop(entry, result_dop_label)
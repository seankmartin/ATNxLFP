# For use with Python doit.
import os


from simuran.main.doit import create_task

# def task_coherence():
#     """Find coherence between regions."""
#     openfield_files = [
#         os.path.join("batch_params", f)
#         for f in os.listdir("batch_params")
#         if "openfield" in f
#     ]
#     mapping_files = [
#         os.path.join("recording_mappings", f)
#         for f in os.listdir("recording_mappings")
#         if "SR" in f
#     ]
#     return {
#         "file_dep": [
#             os.path.join("analysis", "plot_coherence.py"),
#             os.path.join("multi_runs", "coherence_atnx.py"),
#         ]
#         + openfield_files
#         + mapping_files,
#         "targets": [
#             os.path.join("sim_results", "pickles", "coherence_atnx_dump.pickle")
#         ],
#         "actions": [
#             "simuran -r -n 4 -m {}".format(
#                 os.path.join("multi_runs", "coherence_atnx.py")
#             )
#         ],
#         "clean": True,
#         "title": title_with_actions,
#         "verbosity": 0,
#     }


def task_coherence():
    return create_task(
        os.path.join("multi_runs", "coherence_atnx.py"),
        "plot_coherence.py",
        num_workers=4,
    )

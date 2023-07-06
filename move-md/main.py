import argparse
import os
import shutil

# Define the default source directory
default_source_dir = './chatgptbox'

default_golang_dir = './golang'
default_k8s_dir = './k8s'
default_linux_dir = './linux'
default_python_dir = './python'
default_c_dir = './c语言'
default_design_pattern_dir = './design_pattern'
default_javascript_dir = 'JavaScript'
default_git_dir = 'git'
default_data_structure_dir = '数据结构'
default_algorithm_dir = '算法'
prometheus_dir = './prometheus'
default_grpc_dir = 'grpc'

if not os.path.exists(default_golang_dir):
    os.makedirs(default_golang_dir)
if not os.path.exists(default_k8s_dir):
    os.makedirs(default_k8s_dir)
if not os.path.exists(default_linux_dir):
    os.makedirs(default_linux_dir)
if not os.path.exists(default_python_dir):
    os.makedirs(default_python_dir)
if not os.path.exists(default_c_dir):
    os.makedirs(default_c_dir)
if not os.path.exists(default_design_pattern_dir):
    os.makedirs(default_design_pattern_dir)
if not os.path.exists(default_javascript_dir):
    os.makedirs(default_javascript_dir)
if not os.path.exists(default_git_dir):
    os.makedirs(default_git_dir)
if not os.path.exists(default_data_structure_dir):
    os.makedirs(default_data_structure_dir)
if not os.path.exists(default_algorithm_dir):
    os.makedirs(default_algorithm_dir)
if not os.path.exists(prometheus_dir):
    os.makedirs(prometheus_dir)

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--source_dir', type=str,
                    default=default_source_dir, help='Path to source directory')
parser.add_argument('--golang_dir', type=str,
                    default=default_golang_dir, help='Path to golang directory')
parser.add_argument('--k8s_dir', type=str,
                    default=default_k8s_dir, help='Path to k8s directory')
parser.add_argument('--linux_dir', type=str,
                    default=default_linux_dir, help='Path to linux directory')
parser.add_argument('--python_dir', type=str,
                    default=default_python_dir, help='Path to python directory')
parser.add_argument('--c_dir', type=str,
                    default=default_c_dir, help='Path to c directory')
parser.add_argument('--javascript_dir', type=str,
                    default=default_javascript_dir, help='Path to javascript directory')
parser.add_argument('--git_dir', type=str,
                    default=default_git_dir, help='Path to git directory')
args = parser.parse_args()

# Loop through all files in the source directory
for filename in os.listdir(args.source_dir):

    # Check if the file is a markdown file
    if filename.endswith('.md'):
        # Read the contents of the file
        with open(os.path.join(args.source_dir, filename), 'r') as f:
            contents = f.read()

        # Check if the file contains the keyword 'goland'
        if 'goland' in contents or 'GoLand' in contents:
            # Move the file to the golang directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.golang_dir, filename))
        elif '设计模式' in contents or '工厂模式' in contents or '单例模式' in contents or '观察者模式' in contents or '适配器模式' in contents:
            # Move the file to the python directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(default_design_pattern_dir, filename))
        # Check if the file contains the keyword '数据结构'
        elif '数据结构' in contents or '栈' in contents or '队列' in contents or '链表' in contents or '树' in contents or '图' in contents:
            # Move the file to the 数据结构 directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(default_data_structure_dir, filename))
        elif '算法' in contents or 'leetcode' in contents or '回溯' in contents or '剪枝' in contents or 'algorithm' in contents:
            # Move the file to the algorithm directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(default_algorithm_dir, filename))
            # Move files to Prometheus directory
        # Check if the file contains the keyword 'prometheus'
        elif 'prometheus' in contents or 'Prometheus' in contents:
            # Move the file to the prometheus directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(prometheus_dir, filename))
        elif 'protobuf' in contents or 'Protobuf' in contents or 'grpc' in contents or 'gRPC' in contents:
            # Move the file to the prometheus directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(default_grpc_dir, filename))
        elif 'git ' in contents or 'Git ' in contents or 'commit' in contents or 'commit' in contents or 'commit' in contents:
            # Move the file to the git directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.git_dir, filename))
        # Check if the file contains the keyword 'kubectl'
        elif 'kubectl' in contents or 'kubernetes' in contents or 'k8s' in contents or 'deployment' in contents or 'pod' in contents:
            # Move the file to the k8s directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.k8s_dir, filename))
        elif 'linux' in contents or 'tmux' in contents or '进程' in contents or 'yum' in contents or 'Ubuntu' in contents or 'centos' in contents or 'apt' in contents or 'top' in contents:
            # Move the file to the Linux directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.linux_dir, filename))

        # 语言类

        # Check if the file contains the keyword 'golang'
        elif 'golang' in contents or 'Go 语言' in contents or 'Go标准库' in contents or 'goroutine' in contents or 'go语言' in contents:
            # Move the file to the golang directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.golang_dir, filename))
        # Check if the file contains the keyword 'C语言'
        elif 'C语言' in contents or 'C 语言' in contents or 'c语言' in contents or 'c 语言' in contents or 'TCMalloc' in contents or '#include ' in contents:
            # Move the file to the C语言 directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.c_dir, filename))
        # Check if the file contains the keyword '设计模式'
        elif 'javascript' in contents or 'JavaScript' in contents or 'js' in contents or 'npm' in contents or 'node' in contents:
            # Move the file to the javascript directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.javascript_dir, filename))
            # Check if the file contains the keyword 'python'
        elif 'python' in contents or 'Python' in contents or 'py' in contents or 'pip' in contents or 'virtualenv' in contents:
            # Move the file to the python directory
            shutil.move(os.path.join(args.source_dir, filename),
                        os.path.join(args.python_dir, filename))

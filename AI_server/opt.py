import argparse
import torch

parser = argparse.ArgumentParser(description='ML option!')

"----------------------------- General options -----------------------------"
# 18
parser.add_argument('--model_version', dest='model_version', type=str, default='V5',
                    help='model_version')
parser.add_argument('--gpu_model', default=True, type=bool,
                    help='gpu_model')
parser.add_argument('--batch_size', dest='batch_size', type=int,
                    help='batch_size', default=7)
parser.add_argument('--CUDA_VISIBLE_DEVICES', dest='CUDA_VISIBLE_DEVICES', type=str, default='1',
                    help='CUDA_VISIBLE_DEVICES')
parser.add_argument('--anomaly_model_set', dest='anomaly_model_set', nargs='+', default=['mini_AE', 'AE', 'AE_vgg19', 'VAE'],
                    help='anomaly model')
parser.add_argument('--output_n', dest='output_n', type=int,
                    help='output_n', default=2)
parser.add_argument('--image_size', dest='image_size', type=int,
                    help='image_size', default=224)
parser.add_argument('--image_dim', dest='image_dim', type=int,
                    help='image_dim', default=1)

"----------------------------- training options -----------------------------"
# mini_AE/vgg19_1d/AE_vgg19
parser.add_argument('--model_type', dest='model_type', type=str, default='mobile2_1d',
                    help='model_type')
# cross_entropy/L1/L2
parser.add_argument('--loss_type', dest='loss_type', type=str, default='cross_entropy',
                    help='loss_type')
# ['SGD', 0.01, 0.9], ['Adam', 0.0001]
parser.add_argument('--optimizer_type', dest='optimizer_type', nargs='+', default=['Adam', 1e-5],
                    help='optimizer_type')
parser.add_argument('--l2_norm', dest='l2_norm', default=1e-4, type=float,
                    help='l2_norm')
parser.add_argument('--val_proportion', dest='val_proportion', default=0.5, type=float,
                    help='val_proportion')
parser.add_argument('--normal_weight', dest='normal_weight', type=int,
                    help='normal_weight', default=1)
parser.add_argument('--anomaly_weight', dest='anomaly_weight', type=int,
                    help='anomaly_weight', default=20)
parser.add_argument('--loss_lambda', dest='loss_lambda', default=0., type=float,
                    help='loss_lambda')
"----------------------------- validation options -----------------------------"

"----------------------------- testing options --------------------------------"
parser.add_argument('--black_threshold', dest='black_threshold', default=6.9 * 1e-4, type=float,
                    help='black_threshold')


opt = parser.parse_args()
#
# "----------------------------- AlphaPose options -----------------------------"
# parser.add_argument('--addDPG', default=False, type=bool,
#                     help='Train with data augmentation')
# parser.add_argument('--sp', default=False, action='store_true',
#                     help='Use single process for pytorch')
# parser.add_argument('--profile', default=False, action='store_true',
#                     help='add speed profiling at screen output')
#
# "----------------------------- Model options -----------------------------"
# parser.add_argument('--netType', default='hgPRM', type=str,
#                     help='Options: hgPRM | resnext')
# parser.add_argument('--loadModel', default=None, type=str,
#                     help='Provide full path to a previously trained model')
# parser.add_argument('--Continue', default=False, type=bool,
#                     help='Pick up where an experiment left off')
# parser.add_argument('--nFeats', default=256, type=int,
#                     help='Number of features in the hourglass')
# parser.add_argument('--nClasses', default=33, type=int,
#                     help='Number of output channel')
# parser.add_argument('--nStack', default=4, type=int,
#                     help='Number of hourglasses to stack')
#
# "----------------------------- Hyperparameter options -----------------------------"
# parser.add_argument('--fast_inference', default=True, type=bool,
#                     help='Fast inference')
# parser.add_argument('--use_pyranet', default=True, type=bool,
#                     help='use pyranet')
#
# "----------------------------- Hyperparameter options -----------------------------"
# parser.add_argument('--LR', default=2.5e-4, type=float,
#                     help='Learning rate')
# parser.add_argument('--momentum', default=0, type=float,
#                     help='Momentum')
# parser.add_argument('--weightDecay', default=0, type=float,
#                     help='Weight decay')
# parser.add_argument('--crit', default='MSE', type=str,
#                     help='Criterion type')
# parser.add_argument('--optMethod', default='rmsprop', type=str,
#                     help='Optimization method: rmsprop | sgd | nag | adadelta')
#
#
# "----------------------------- Training options -----------------------------"
# parser.add_argument('--nEpochs', default=50, type=int,
#                     help='Number of hourglasses to stack')
# parser.add_argument('--epoch', default=0, type=int,
#                     help='Current epoch')
# parser.add_argument('--trainBatch', default=40, type=int,
#                     help='Train-batch size')
# parser.add_argument('--validBatch', default=20, type=int,
#                     help='Valid-batch size')
# parser.add_argument('--trainIters', default=0, type=int,
#                     help='Total train iters')
# parser.add_argument('--valIters', default=0, type=int,
#                     help='Total valid iters')
# parser.add_argument('--init', default=None, type=str,
#                     help='Initialization')
#
# "----------------------------- Data options -----------------------------"
# parser.add_argument('--inputResH', default=320, type=int,
#                     help='Input image height')
# parser.add_argument('--inputResW', default=256, type=int,
#                     help='Input image width')
# parser.add_argument('--outputResH', default=80, type=int,
#                     help='Output heatmap height')
# parser.add_argument('--outputResW', default=64, type=int,
#                     help='Output heatmap width')
# parser.add_argument('--scale', default=0.25, type=float,
#                     help='Degree of scale augmentation')
# parser.add_argument('--rotate', default=30, type=float,
#                     help='Degree of rotation augmentation')
# parser.add_argument('--hmGauss', default=1, type=int,
#                     help='Heatmap gaussian size')
#
#
# "----------------------------- PyraNet options -----------------------------"
# parser.add_argument('--baseWidth', default=9, type=int,
#                     help='Heatmap gaussian size')
# parser.add_argument('--cardinality', default=5, type=int,
#                     help='Heatmap gaussian size')
# parser.add_argument('--nResidual', default=1, type=int,
#                     help='Number of residual modules at each location in the pyranet')
#
# "----------------------------- Distribution options -----------------------------"
# parser.add_argument('--dist', dest='dist', type=int, default=1,
#                     help='distributed training or not')
# parser.add_argument('--backend', dest='backend', type=str, default='gloo',
#                     help='backend for distributed training')
# parser.add_argument('--port', dest='port',
#                     help='port of server')
#
# "----------------------------- Detection options -----------------------------"
# parser.add_argument('--net', dest='demo_net', help='Network to use [vgg16 res101]',
#                     default='res152')
# parser.add_argument('--indir', dest='inputpath',
#                     help='image-directory', default="")
# parser.add_argument('--list', dest='inputlist',
#                     help='image-list', default="")
# parser.add_argument('--mode', dest='mode',
#                     help='detection mode, fast/normal/accurate', default="normal")
# parser.add_argument('--outdir', dest='outputpath',
#                     help='output-directory', default="examples/res/")
# parser.add_argument('--inp_dim', dest='inp_dim', type=str, default='608',
#                     help='inpdim')
# parser.add_argument('--conf', dest='confidence', type=float, default=0.05,
#                     help='bounding box confidence threshold')
# parser.add_argument('--nms', dest='nms_thesh', type=float, default=0.6,
#                     help='bounding box nms threshold')
# parser.add_argument('--save_img', default=False, action='store_true',
#                     help='save result as image')
# parser.add_argument('--vis', default=False, action='store_true',
#                     help='visualize image')
# parser.add_argument('--matching', default=False, action='store_true',
#                     help='use best matching')
# parser.add_argument('--format', type=str,
#                     help='save in the format of cmu or coco or openpose, option: coco/cmu/open')
# parser.add_argument('--detbatch', type=int, default=1,
#                     help='detection batch size')
# parser.add_argument('--posebatch', type=int, default=80,
#                     help='pose estimation maximum batch size')
# parser.add_argument('--point_threshold_score', type=float, default=0.05,
#                     help='threshold of trust for the point on pose')
#
# "----------------------------- Video options -----------------------------"
# parser.add_argument('--video', dest='video',
#                     help='video-name', default="")
# parser.add_argument('--webcam', dest='webcam', type=str,
#                     help='webcam number', default='0')
# parser.add_argument('--save_video', dest='save_video',
#                     help='whether to save rendered video', default=False, action='store_true')
# parser.add_argument('--vis_fast', dest='vis_fast',
#                     help='use fast rendering', action='store_true', default=True)
# parser.add_argument('--local_i', dest='local_i', nargs='+', default='',
#                     help='Select the starting cutting range')
# parser.add_argument('--local_f', dest='local_f', nargs='+', default='',
#                     help='Select the ending cutting range')
# parser.add_argument('--local_check', dest='local_check',default=False,
#                     help='check cutting range', action='store_true')
# parser.add_argument('--track', dest='track', nargs='+', default='',
#                     help='track the points')
# parser.add_argument('--dis_img', dest='dis_img', nargs='+', default='',
#                     help='display the size of image')
# parser.add_argument('--shift', dest='shift', type=int,
#                     help='shift frames', default='0')
#
# "----------------------------- yolo -----------------------------"
# parser.add_argument('--yolo_batchsize', dest='yolo_batchsize', type=int,
#                     help='yolo batchsize', default='1')
#
# "----------------------------- os -----------------------------"
# parser.add_argument('--os', dest='os', type=str, default='linux',
#                     help='check your system')
# "----------------------------- gpu -----------------------------"
# parser.add_argument('--gpu', dest='gpu', type=str, default='',
#                     help='The model run on this gpu!')

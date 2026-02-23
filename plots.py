import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

def plot_training_log(csv_file, output_dir='./plots'):
    os.makedirs(output_dir, exist_ok=True)
    
    # 读取CSV文件
    df = pd.read_csv(csv_file)
    
    # 过滤掉可能缺失的行（如相对误差列可能为空）
    # 损失曲线（迭代次数 vs 损失值）
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 子图1：总损失、c损失、e损失
    ax = axes[0, 0]
    ax.plot(df['iter'], df['total_loss'], label='Total Loss')
    ax.plot(df['iter'], df['loss_c'], label='Loss_c (concentration)')
    ax.plot(df['iter'], df['loss_e'], label='Loss_e (equation residuals)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Loss')
    ax.set_yscale('log')  # 损失通常呈指数下降，使用对数坐标更清晰
    ax.legend()
    ax.grid(True)
    ax.set_title('Training Losses')
    
    # 子图2：各方程残差损失
    ax = axes[0, 1]
    ax.plot(df['iter'], df['loss_e1'], label='e1 (c transport)')
    ax.plot(df['iter'], df['loss_e2'], label='e2 (x-momentum)')
    ax.plot(df['iter'], df['loss_e3'], label='e3 (y-momentum)')
    ax.plot(df['iter'], df['loss_e4'], label='e4 (continuity)')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Loss')
    ax.set_yscale('log')
    ax.legend()
    ax.grid(True)
    ax.set_title('Equation Residual Losses')
    
    # 子图3：相对L2误差（需去除NaN行）
    df_err = df.dropna(subset=['c_relL2']).copy()
    if not df_err.empty:
        ax = axes[1, 0]
        ax.plot(df_err['iter'], df_err['c_relL2'], label='c')
        ax.plot(df_err['iter'], df_err['u_relL2'], label='u')
        ax.plot(df_err['iter'], df_err['v_relL2'], label='v')
        ax.plot(df_err['iter'], df_err['p_relL2'], label='p')
        ax.set_xlabel('Iteration')
        ax.set_ylabel('Relative L2 Error')
        ax.legend()
        ax.grid(True)
        ax.set_title('Test Relative L2 Errors')
    else:
        axes[1, 0].text(0.5, 0.5, 'No error data', ha='center', va='center')
    
    # 子图4：可留空或绘制损失比例等
    axes[1, 1].axis('off')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'training_curves.png'), dpi=150)
    plt.show()
    print(f"Plot saved to {os.path.join(output_dir, 'training_curves.png')}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_file', type=str, required=True, help='Path to the training log CSV file')
    parser.add_argument('--output_dir', type=str, default='./plots', help='Directory to save plots')
    args = parser.parse_args()
    plot_training_log(args.log_file, args.output_dir)
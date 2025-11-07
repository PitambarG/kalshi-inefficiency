
import matplotlib.pyplot as plt

def plot_market_vs_model(times, p_market, p_model, title="Market vs Model Probability"):
    plt.figure()
    plt.plot(times, p_market, label="Market (Implied)")
    plt.plot(times, p_model, label="Model (Predicted)")
    plt.xlabel("Time")
    plt.ylabel("Probability")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.show()

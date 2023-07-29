# x to the power of x: a complex story

Curious about the visual representation of x to the power of x? Step into the captivating universe of complex number with complex exponentiation, where boundaries are pushed, and knowledge expands exponentially!

This project aims to visualize the function $y = x^x$ in the complex plane and explain the math behind the generation. My approach to this problem is mostly inspired by [李永乐老师@tchliyongle](https://www.youtube.com/watch?v=6HYZWVYv0WY), a prominent science popularizer and educational video creator from China. During my research of the problem, I also stumbled across this amazing [post](https://mathematica.stackexchange.com/questions/10594/how-can-i-plot-the-complex-graph-of-xx-in-mathematica/10598#10598?newreg=5f48d5db821a4a2c9e145a78b423052d) on stackexchange. I hope this repository can capture the esscences of this problem and help other math enthusiasts from all levels to engage with it.

## How it works

The function $y = x^x$, while simple in the real number domain, exhibits fascinating properties when extended to the complex plane.The key to understanding these properties lies in Euler's formula, the definition of complex exponentiation, and the multi-valued nature of complex functions. In the code, I use these concepts to define $y = x^x$ in the complex plane and explore its behavior for different integer values of k, which correspond to different "branches" of the multi-valued function. If you need a review or the concepts sound new, you can checkout my math explanation files (still working on it!) where I explain the motivations and elaborate on each step that leads to the final result.

## Files

- `x-power-x.py`: This is the main Python script that generates the x to the power x visualizations.
- `x-power-x.nb`: This is the mathematica notebook that generates the x to the power x visualizations. (You need to have mathematica installed to run this notebook after downloading)
- `negative1-power-x.py`: This is the Python script that generates the -1 to the power x visualizations.
- `math-explanation.tex`: The latex file for the report (still working on it!)
- `math-explanation.pdf`: A report that contains my research and report to the problem (still working on it!)

## Visualizations

The Python script generates two types of visualizations:

1. A 3D plot of the real and imaginary parts of y = x^x for different k values in Python. This plot shows how the function behaves in the complex plane.

   ![3D plot](x-power-x.png)

2. A 2D plot of the imaginary part of y = x^x against x for different k values in Python. This plot shows how the imaginary part of the function changes with x.

   ![2D plot](x-power-x-imaginary_vs_x.png)

The Mathematica Notebook contains similar plots and also includes some other information that can be used to help understand the different properties of the graph.

## Usage

To generate the visualizations, simply run the `x-power-x.py` script:

```bash
python x-power-x.py
```

## Dependencies

This script requires the following Python libraries, which are listed in the `requirements.txt` file:

- NumPy
- Matplotlib

You can install these libraries using pip:

```bash
pip install -r requirements.txt
```

## Exploration, Collaboration, and Future Development

This is one of my math explorations that delve into the complex behavior of the function $y=x^x$. I invite you to join me in this exciting journey by experimenting with the code, tweaking parameters, and observing the fascinating outcomes.

If you have any suggestions for improving the project, intriguing observations to share, or you encounter any issues while using the code, please let me know. You can submit your suggestions, feedback, or bug reports as issues/pull requests right here on this repository. I value your input and am eager to collaborate with you to make this project even better.

For future directions, I am interested in adding more customization options for the visualizations or creating interactive visualizations, but those will be not my top priority for now.

Feel free to reach out to me at patricsu3675@gmail.com and let us unlock more hidden wonders of mathematics

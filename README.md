# Reads GAN

A PyTorch implementation of Generative Adversarial Networks (GANs) for generating biological sequence reads, specifically designed for DNA/RNA sequence generation and analysis.

## Overview

This project implements a sequence-based GAN that can generate realistic biological sequences (DNA/RNA reads) using adversarial training. The model is based on the SeqGAN architecture and includes specialized components for handling biological sequence data, including k-mer analysis, CIGAR string processing, and sequence alignment evaluation.

## Features

- **Sequence Generation**: Generate realistic DNA/RNA sequences using GAN architecture
- **K-mer Analysis**: Process and analyze k-mer distributions in biological sequences
- **CIGAR String Processing**: Parse and analyze CIGAR strings from sequence alignments
- **Benchmarking Tools**: Comprehensive evaluation and comparison tools
- **FASTA Processing**: Utilities for reading and writing FASTA format files
- **Edit Pattern Analysis**: Analyze insertion, deletion, and match patterns in sequences

## Project Structure

```
reads_GAN/
├── src/
│   ├── models/           # Core GAN model components
│   │   ├── generator.py  # Generator network
│   │   ├── discriminator.py  # Discriminator network
│   │   ├── lstmCore.py   # LSTM core implementation
│   │   └── rollout.py    # Rollout policy for training
│   ├── data/             # Data processing utilities
│   │   ├── data_processing.py  # Main data processing functions
│   │   └── kmer.py       # K-mer analysis tools
│   └── utils/            # Utility functions
│       └── fasta.py      # FASTA file processing
├── benchmark/            # Evaluation and analysis tools
│   ├── notebooks/        # Jupyter notebooks for analysis
│   │   ├── baseline.ipynb
│   │   └── parse_cigar.ipynb
│   ├── scripts/          # Analysis scripts
│   └── data/             # Benchmark datasets
├── code/                 # Legacy code (to be cleaned up)
├── repo/                 # Model checkpoints and data
├── figures/              # Generated figures and plots
├── sequence_GAN.py       # Main training script
├── sequence_GAN_generate.py  # Generation script
├── config.py             # Configuration settings
└── requirements.txt      # Python dependencies
```

## Usage

### Training the Model

To train the sequence GAN:

```bash
python sequence_GAN.py [batch_size]
```

Example:
```bash
python sequence_GAN.py 32
```

### Generating Sequences

To generate new sequences using a trained model:

```bash
python sequence_GAN_generate.py [batch_size]
```

Example:
```bash
python sequence_GAN_generate.py 10
```

### K-mer Analysis

The project includes tools for k-mer analysis:

```python
from src.data.kmer import KmerAnalyzer

analyzer = KmerAnalyzer(k=6)
kmers = analyzer.extract_kmers("sequence.fasta")
distribution = analyzer.get_kmer_distribution(kmers)
```

### CIGAR String Processing

Analyze CIGAR strings from sequence alignments:

```python
from benchmark.scripts.parse_cigar import CigarAnalyzer

analyzer = CigarAnalyzer()
match_counts, deletion_counts, insertion_counts = analyzer.count_operations(cigars)
```

## Configuration

Key configuration parameters in `config.py`:

- `SEQ_LENGTH`: Maximum sequence length (default: 96)
- `VOCAB_SIZE`: Vocabulary size for k-mers
- `BATCH_SIZE`: Training batch size
- `GEN_EPOCHS`: Generator training epochs
- `DIS_EPOCHS`: Discriminator training epochs
- `DEVICE`: Computing device (cuda/cpu)

## Benchmarking

The `benchmark/` directory contains tools for evaluating generated sequences:

1. **Baseline Analysis** (`notebooks/baseline.ipynb`): Compare generated sequences with real data
2. **CIGAR Analysis** (`notebooks/parse_cigar.ipynb`): Analyze alignment patterns
3. **K-mer Distribution** (`scripts/kmer_distribution.py`): Compare k-mer distributions

## Model Architecture

The GAN consists of:

- **Generator**: LSTM-based network that generates sequences token by token
- **Discriminator**: CNN-based network that classifies sequences as real or generated
- **Rollout Policy**: Monte Carlo tree search for training the generator

## Data Format

The model expects data in the following formats:

- **FASTA files**: Standard biological sequence format
- **K-mer files**: Pickled k-mer sequences
- **CIGAR strings**: SAM format alignment strings

## Examples

### Basic Sequence Generation

```python
import torch
from sequence_GAN_generate import main

# Generate 10 sequences
sequences = main(batch_size=10)
print(f"Generated {len(sequences)} sequences")
```

### K-mer Analysis

```python
from src.data.kmer import extract_kmers, analyze_distribution

# Extract 6-mers from a sequence
kmers = extract_kmers("ATCGATCGATCG", k=6)
distribution = analyze_distribution(kmers)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is based on the SeqGAN implementation. Please refer to the original SeqGAN paper and repository for licensing information.

## Troubleshooting

### Common Issues

1. **CUDA out of memory**: Reduce batch size in config.py
2. **Import errors**: Ensure all dependencies are installed
3. **File not found**: Check that data files are in the correct directories

### Performance Tips

- Use GPU acceleration when available
- Adjust batch size based on available memory
- Use smaller vocabulary sizes for faster training

## Future Work

- [ ] Add support for protein sequences
- [ ] Implement attention mechanisms
- [ ] Add more sophisticated evaluation metrics
- [ ] Optimize for larger sequence lengths
- [ ] Add support for paired-end reads
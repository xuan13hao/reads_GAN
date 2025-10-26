#!/usr/bin/env python3
"""
Basic usage example for Reads GAN
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import torch
from src.data.kmer import extract_kmers
from src.utils.fasta import read_fasta

def main():
    """
    Basic example of using the Reads GAN
    """
    print("Reads GAN - Basic Usage Example")
    print("=" * 40)
    
    # Example 1: Extract k-mers from a sequence
    print("\n1. K-mer Extraction Example:")
    sequence = "ATCGATCGATCG"
    k = 6
    kmers = extract_kmers(sequence, k)
    print(f"Sequence: {sequence}")
    print(f"K-mers (k={k}): {kmers}")
    
    # Example 2: Load a trained model (if available)
    print("\n2. Model Loading Example:")
    model_path = "repo/generator.pkl"
    if os.path.exists(model_path):
        try:
            model = torch.load(model_path, map_location='cpu')
            print(f"Successfully loaded model from {model_path}")
            print(f"Model type: {type(model)}")
        except Exception as e:
            print(f"Error loading model: {e}")
    else:
        print(f"Model file not found at {model_path}")
        print("Please train a model first using: python sequence_GAN.py")
    
    # Example 3: Generate sequences (if model is available)
    print("\n3. Sequence Generation Example:")
    if 'model' in locals():
        try:
            # Generate a small batch
            batch_size = 3
            generated = model.generate(batch_size=batch_size)
            print(f"Generated {batch_size} sequences")
            print("Note: Generated sequences are in token format")
        except Exception as e:
            print(f"Error generating sequences: {e}")
    else:
        print("No model available for generation")
    
    print("\n" + "=" * 40)
    print("Example completed!")

if __name__ == "__main__":
    main()
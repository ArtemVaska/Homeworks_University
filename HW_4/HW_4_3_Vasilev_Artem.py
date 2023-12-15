"""
3. Создать классы, описывающие биологические последовательности ДНК, РНК, белков,
наследующие от общего класса «последовательность». Каждый класс должен иметь свойство алфавит,
уметь возвращать название последовательности, саму последовательность, ее длину, статистику
по использованию в ней символов, ее молекулярную массу, а также специфичные функции (возврат
комплементарной последовательности, транскрипция ДНК --> РНК, трансляция РНК --> белок)
"""


def make_class(seq: str):
    seq_init = Sequence(seq)
    if seq_init.which_seq == 'dna':
        seq = DnaSequence(seq)
    elif seq_init.which_seq == 'rna':
        seq = RnaSequence(seq)
    elif seq_init.which_seq == 'protein':
        seq = ProteinSequence(seq)
    return seq


class Sequence:
    DNA_ALPHABET = 'ATGCatgc'
    RNA_ALPHABET = 'AUGCaugc'
    PROTEIN_ALPHABET = 'ACDEFGHIKLMNPQRSTVWYacdefghiklmnpqrstvwy'
    COMPLEMENT_ALPHABET = {
        'A': 'T', 'a': 't',
        'G': 'C', 'g': 'c',
        'T': 'A', 't': 'a',
        'C': 'G', 'c': 'g',
        'U': 'A', 'u': 'a'
    }

    def __init__(self, seq: str):
        self.seq = seq

    @property
    def get_alphabet(self):
        return sorted(set(self.seq))

    @property
    def which_seq(self):
        if set(self.seq) <= set(self.DNA_ALPHABET):
            return 'dna'
        elif set(self.seq) <= set(self.RNA_ALPHABET):
            return 'rna'
        elif set(self.seq) <= set(self.PROTEIN_ALPHABET):
            return 'protein'

    @property
    def get_seq(self):
        return self.seq

    @property
    def get_length(self):
        return len(self.seq)

    @property
    def complement(self):
        complement_seq = ''
        for nucleotide in self.seq:
            complement_seq += self.COMPLEMENT_ALPHABET[nucleotide]
        return complement_seq


class DnaSequence(Sequence):
    TRANSCRIBE_ALPHABET = {
        'T': 'U', 't': 'u',
        'U': 'T', 'u': 't'
    }

    def __init__(self, seq: str):
        super().__init__(seq)

    @property
    def transcribe(self):
        transcribed_seq = ''
        for nucleotide in self.seq:
            if nucleotide in self.TRANSCRIBE_ALPHABET:
                transcribed_seq += self.TRANSCRIBE_ALPHABET[nucleotide]
            else:
                transcribed_seq += nucleotide
        return transcribed_seq


class RnaSequence(Sequence):
    TRANSLATE_ALPHABET = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    def __init__(self, seq: str):
        super().__init__(seq)

    @property
    def translate(self):
        if len(self.seq) % 3 != 0:
            raise ValueError('Последовательность РНК должна быть кратка 3-м')

        translated_seq = ''

        process_seq = self.seq
        while len(process_seq) >= 3:
            codon = process_seq[:3]
            translated_seq += self.TRANSLATE_ALPHABET[codon]
            process_seq = process_seq[3:]

        return translated_seq


class ProteinSequence(Sequence):
    def __init__(self, seq: str):
        super().__init__(seq)


seq1 = make_class('ATGC')
seq2 = make_class('AUGCCCAUGCCCAUGCCCAUGCCC')
seq3 = make_class('ACDEACDE')

print(seq1.get_alphabet)
print(seq1.get_seq)
print(seq1.complement)
print(seq1.transcribe)
print()
print(seq2.translate)
print()
print(seq3.which_seq)

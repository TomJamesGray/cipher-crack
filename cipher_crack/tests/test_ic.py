from cipher_crack.crack import calculate_ic

def test_ic():
    text = """Permission is hereby granted, free of charge, to any person obtaining a copyof this software and associated documentation files (the "Software"), to dealin the Software without restriction, including without limitation the rightsto use, copy, modify, merge, publish, distribute, sublicense, and/or sellcopies of the Software, and to permit persons to whom the Software isfurnished to do so, subject to the following conditions:The above copyright notice and this permission notice shall be included in allcopies or substantial portions of the Software.THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS ORIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THEAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHERLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THESOFTWARE."""
    expected_ic = 1.75561523
    assert round(calculate_ic(text),8) == expected_ic

def test_ic_special_chars():
    text = """Linus Benedict Torvalds (/ˈlaɪnəsˈtɔːrvɔːldz/;[5] Swedish: [ˈliːn.ɵs ˈtuːr.valds] ( listen); born December 28, 1969) is a Finnish software engineer[2][6] who is the creator and, for a long time, principal developer, of the Linux kernel; which became the kernel for operating systems such as the Linux operating system, Android and Chrome OS. He also created the distributed revision control system Git and the diving logging and planning software Subsurface. He was honored, along with Shinya Yamanaka, with the 2012 Millennium Technology Prize by the Technology Academy Finland "in recognition of his creation of a new open source operating system for computers leading to the widely used Linux kernel".[7] He is also the recipient of the 2014 IEEE Computer Society Computer Pioneer Award.[8]"""
    expected_ic = 1.64799956
    print(calculate_ic(text))
    assert round(calculate_ic(text),8) == expected_ic

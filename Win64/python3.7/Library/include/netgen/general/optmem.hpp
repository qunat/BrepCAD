#ifndef FILE_OPTMEM
#define FILE_OPTMEM

/**************************************************************************/
/* File:   optmem.hh                                                      */
/* Author: Joachim Schoeberl                                              */
/* Date:   04. Apr. 97                                                    */
/**************************************************************************/

namespace netgen
{

/** 
    Optimized Memory allocation classes
*/

class BlockAllocator
{
private:
  ///
  unsigned size, blocks;
  ///
  void * freelist;
  ///
  NgArray<char*> bablocks;
  mutex block_allocator_mutex;
public:
  ///
  BlockAllocator (unsigned asize, unsigned ablocks = 100);
  ///
  ~BlockAllocator ();
  ///

  void * Alloc ();
  /*
  {
    if (!freelist)
      Alloc2();

    void * p = freelist;
    // freelist = *(void**)freelist;
    freelist = *static_cast<void**> (freelist);

    return p;
  }
  */


  ///
  void Free (void * p);
  /*
  {
    if (!bablocks.Size()) return;
    *(void**)p = freelist;
    freelist = p;
  }
  */


private:
  //  void Alloc2 ();
};

}

#endif
